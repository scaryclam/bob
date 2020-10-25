import threading
import time
import logging
from datetime import datetime, timedelta

from job_manager.services import JobService


def clean():
    service = JobService()

    while True:
        print("Cleaning")
        now = datetime.now()
        active_jobs = service.get_active_jobs()
        for job in active_jobs:
            deadline = now - timedelta(
                seconds=job.harakiri_delta_seconds)
            if job.modified < deadline:
                # Kill the job, it's too old
                service.set_job_status(job, 'dead')

        time.sleep(5)


def start_cleaner():
    thread = threading.Thread(target=clean)
    thread.start()
