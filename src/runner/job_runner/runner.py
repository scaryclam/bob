import logging
import json

from job_runner.amqp.consumer import AMQPConsumer
from job_runner.amqp.publisher import AMQPPublisher


logger = logging.getLogger("runner")


class Runner:
    def start(self):
        self._start_consumer()

    def _start_consumer(self):
        host = '127.0.0.1'
        vhost = '/'

        # Examples to use with the vagrant setup.
        # TODO: config file
        user = 'manager'
        password = 'vagrant'
        exchange = 'bob-jobs'
        queue = 'execute'
        callback = self.callback

        consumer = AMQPConsumer()
        consumer.start(host, vhost, user, password, exchange, queue, callback)

    def callback(self, message, consumer):
        host = '127.0.0.1'
        vhost = '/'
        user = 'manager'
        password = 'vagrant'
        exchange = 'bob'
        queue = 'job'

        logger.critical("Got a callback")
        job_id = message.get('job_id')

        publisher = AMQPPublisher(
            host, vhost, user, password, exchange, queue)
        publisher.publish_message({"job_id": str(job_id),
                                   "new-status": "running",
                                   "command": "update"})
