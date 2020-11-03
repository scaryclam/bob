import json
import pika
import logging

# Set up a logger
logger = logging.getLogger("publisher")


class AMQPPublisher:
    def __init__(self, host, vhost, user, password, exchange, queue):
        connected = False

        self.host = host
        self.vhost = vhost
        self.user = user
        self.password = password
        self.exchange = exchange
        self.queue = queue

    def setup(self):
        publisher_connection, publisher_channel = self._create_publisher(
            self.host, self.vhost, self.user, self.password)
        publisher_channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='direct')

        # Make sure there's a queue, otherwise published jobs go into the
        # ether
        result = publisher_channel.queue_declare(self.queue, durable=True)
        publisher_channel.queue_bind(
            exchange=self.exchange,
            routing_key=self.queue,
            queue=result.method.queue)

        self.channel = publisher_channel
        self.publisher_connection = publisher_connection

    def _create_publisher(self, host, vhost, user, password):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host,
            virtual_host=vhost,
            credentials=pika.credentials.PlainCredentials(user, password)))
        channel = connection.channel()
        return connection, channel

    def publish_message(self, message):
        try:
            self.channel.basic_publish(
                exchange=self.exchange,
                routing_key=self.queue,
                body=json.dumps(message, ensure_ascii=False),
                properties=pika.BasicProperties(
                    content_type='text/plain',
                    delivery_mode=2))

        except (AttributeError, pika.exceptions.ConnectionClosed):
            self.setup()
            self.publish_message(message)
        except Exception:
            logger.exception("Unable to publish to queue")
            raise
        else:
            logger.critical(
                "Successful send to exchange. Message: %s", message)
            return True

    def close_all(self):
        logger.warn("Closing connection")
        try:
            self.publisher_connection.close()
        except Exception:
            logger.exception("Error closing connection")
