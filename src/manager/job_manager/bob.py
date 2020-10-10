import logging

from job_manager.amqp.consumer import AMQPConsumer


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

    def callback(self, *args, **kwargs):
        logger.critical("Got a callback")

