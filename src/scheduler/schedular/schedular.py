import sched
import uuid
from datetime import datetime
from time import time, sleep

from croniter import croniter

from amqp.publisher import AMQPPublisher


class Job:
    def __init__(self, job_config):
        self.job_id = str(uuid.uuid4())
        self.cron_config = job_config['schedule']
        self.message = job_config['message']
        self.name = job_config['name']
        self.cron = croniter(self.cron_config, datetime.now())
        self.next_schedule = None
        self.publisher = self._make_publisher(
            job_config['host'],
            job_config['vhost'],
            job_config['user'],
            job_config['password'],
            job_config['exchange'],
            job_config['target_queue'])

    def _make_publisher(self, host, vhost, user, password, exchange, queue):
        publisher = AMQPPublisher(
            host, vhost, user, password, exchange, queue)
        return publisher

    def publish_job(self):
        self.publisher.publish_message({"job_id": self.job_id,
                                        "name": self.name,
                                        "message": self.message})

    def get_next_run_time(self):
        if self.next_schedule is None:
            self.next_schedule = self.cron.get_next()
        return self.next_schedule

    def create_config(self):
        config = {
            'name': self.name,
            'message': self.message,
            'schedule': self.cron_config,
            'target_queue': 'execute',
            'vhost': '/',
            'host': '127.0.0.1',
            'user': 'manager',
            'password': 'vagrant',
            'exchange': 'bob-jobs',
        }
        return config

    def run(self, scheduler_callback, **kwargs):
        print(f"Running job {self.job_id} ({self.name})")
        self.publish_job()
        scheduler_callback(self.create_config(), self.job_id)


class Schedular:
    jobs = None
    scheduler = None
    exit = False

    def add_job(self, job_config):

        if self.scheduler is None:
            self.scheduler = sched.scheduler(time, sleep)

        job = Job(job_config)

        next_run = job.get_next_run_time()
        event = self.scheduler.enterabs(
            next_run, 1, job.run, argument=(self.callback, ))

        if self.jobs is None:
            self.jobs = {job.job_id: {'event': event, 'job': job}}
        else:
            self.jobs[job.job_id] = {'event': event, 'job': job}

    def start(self, schedule):
        # Read the config for things to schedule
        for job in schedule:
            print(f'Adding {job["name"]}')
            self.add_job(job)
        self.run_loop()

    def callback(self, job_config, previous_job_id):
        self.jobs.pop(previous_job_id)
        self.add_job(job_config)

    def run_loop(self):
        while not self.exit:
            self.scheduler.run()
            sleep(1)
