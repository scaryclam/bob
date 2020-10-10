import json
import pika
import logging
import time


# Set up a logger
logger = logging.getLogger("consumer")


class AMQPConsumer:
    queue = None
    exchange = None
    host = None
    vhost = None
    callback = None

    def start(self, host, vhost, user, password, exchange, queue, callback):
        connected = False

        self.host = host
        self.vhost = vhost
        self.user = user
        self.password = password
        self.exchange = exchange
        self.queue_name = queue
        self.callback = callback

        while not connected:
            logger.critical("Connection starting...")
            try:
                connected = True
                # Consumer
                self._setup_consumer()
            except Exception as err:
                logger.critical("Connection failed")
                connected = False
                logger.critical("Will try to reconnect in 5 seconds...")
                time.sleep(5)

    def _setup_consumer(self):
        consumer_connection, consumer_channel = self._create_consumer(
            self.host, self.vhost, self.user, self.password, self.queue_name)

        self.consumer_channel = consumer_channel
        self.consumer_connection = consumer_connection

        logger.critical(f"Connection created to {self.queue_name}, listening")
        self._listen()

    def _create_consumer(self, host, vhost, user, password, queue_name):
        consumer_connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host,
            virtual_host=vhost,
            credentials=pika.credentials.PlainCredentials(user, password)))
        consumer_channel = consumer_connection.channel()

        consumer_channel.exchange_declare(
            exchange=self.exchange, exchange_type='direct')

        consumer_channel.queue_declare(queue=queue_name, durable=True)
        result = consumer_channel.queue_bind(
            exchange=self.exchange, queue=queue_name)

        return consumer_connection, consumer_channel

    def _listen(self):

        try:
            self.consumer_channel.basic_consume(
                self.queue_name,
                self._process_message,
                auto_ack=False)
            self.consumer_channel.start_consuming()
        except Exception as err:
            logger.exception("An error occured! Bailing!")
            self.close_all()
            raise

    def _process_message(self, channel, method, properties, body):
        try:
            message = json.loads(body.decode("utf-8"))
            self.callback(message, self)
        except Exception as err:
            logger.exception("An error occured! Bailing!")
            return

        # No errors raised means we're safe to ack
        self._consumer_ack(method.delivery_tag, message)

    def _consumer_ack(self, delivery_tag, message):
        try:
            self.consumer_channel.basic_ack(delivery_tag=delivery_tag)
        except Exception as error:
            logger.exception(
                "Could not ack message from queue! Message: %s", message)
            raise

    def _close_all(self):
        try:
            self.consumer_connection.close()
        except Exception:
            logger.exception("Error closing the connection!")
