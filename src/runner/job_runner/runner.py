import logging
import json

from job_runner.amqp.consumer import AMQPConsumer
from job_runner.amqp.publisher import AMQPPublisher
import settings


logger = logging.getLogger("runner")


class Runner:
    def start(self):
        self._start_consumer()

    def _start_consumer(self):
        host = settings.RABBITMQ['consumer']['HOST']
        vhost = settings.RABBITMQ['consumer']['VHOST']

        user = settings.RABBITMQ['consumer']['USER']
        password = settings.RABBITMQ['consumer']['PASSWORD']
        exchange = settings.RABBITMQ['consumer']['EXCHANGE']
        queue = settings.RABBITMQ['consumer']['QUEUE']

        callback = self.callback

        consumer = AMQPConsumer()
        consumer.start(host, vhost, user, password, exchange, queue, callback)

    def callback(self, message, consumer):
        host = settings.RABBITMQ['publisher']['HOST']
        vhost = settings.RABBITMQ['publisher']['VHOST']

        user = settings.RABBITMQ['publisher']['USER']
        password = settings.RABBITMQ['publisher']['PASSWORD']
        exchange = settings.RABBITMQ['publisher']['EXCHANGE']
        queue = settings.RABBITMQ['publisher']['QUEUE']

        logger.critical("Got a callback")
        job_id = message.get('job_id')

        publisher = AMQPPublisher(
            host, vhost, user, password, exchange, queue)
        publisher.publish_message({"job_id": str(job_id),
                                   "new-status": "running",
                                   "command": "update"})
