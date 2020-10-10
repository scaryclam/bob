import logging

from job_manager.amqp.consumer import AMQPConsumer
from job_manager.services import JobService


logger = logging.getLogger('bob-manager')


class Bob:
    def start(self):
        host = '127.0.0.1'
        vhost = '/'

        # Examples to use with the vagrant setup.
        # TODO: config file
        user = 'manager'
        password = 'vagrant'
        exchange = 'bob'
        queue = 'jobs'
        callback = self.callback

        consumer = AMQPConsumer()
        consumer.start(host, vhost, user, password, exchange, queue, callback)

    def callback(self, message, consumer):
        logger.critical("Got a callback")
        if message.get('command', 'create'):
            self._create_job(message)

    def _create_job(self, job_message):
        service = JobService()
        service.create_job(job_message['job_name'])
