import logging
import json

from job_manager.amqp.consumer import AMQPConsumer
from job_manager.amqp.publisher import AMQPPublisher
from job_manager.services import JobService
from job_manager.cleaner import start_cleaner
import settings

logger = logging.getLogger('bob-manager')



class Bob:
    def start(self):
        self._start_cleaner()
        self._start_consumer()

    def _start_cleaner(self):
        start_cleaner()

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
        logger.critical("Got a callback")
        command = message.get('command')
        if command == 'create':
            logger.critical("Creating Job")
            self._start_job(message)
        elif command == 'update':
            logger.critical("Updating Job")
            self._update_job(message)

    def _start_job(self, job_message):
        host = settings.RABBITMQ['publisher']['HOST']
        vhost = settings.RABBITMQ['publisher']['VHOST']
        user = settings.RABBITMQ['publisher']['USER']
        password = settings.RABBITMQ['publisher']['PASSWORD']
        exchange = settings.RABBITMQ['publisher']['EXCHANGE']
        queue = settings.RABBITMQ['publisher']['QUEUE']

        service = JobService()
        job = service.create_job(job_message['job_name'])
        publisher = AMQPPublisher(
            host, vhost, user, password, exchange, queue)
        publisher.publish_message({"job_id": str(job.job_id)})
        service.set_job_status(job, "queued")

    def _update_job(self, job_message):
        service = JobService()

        job_id = job_message['job_id']
        job = service.get_job(job_id)

        status = 'running'
        if job_message.get("new-status", False):
            status = job_message['new-status']

        service.update_job(job, status)
