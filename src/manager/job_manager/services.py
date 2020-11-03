from datetime import datetime
from uuid import uuid4

from job_manager.models import Job


class JobService:
    def create_job(self, name, harakiri_delta_seconds=30):
        uuid = uuid4()
        created = datetime.now()
        modified = datetime.now()

        new_job = Job(
            name=name,
            job_id=uuid,
            status="created",
            harakiri_delta_seconds=harakiri_delta_seconds,
            created=created,
            modified=modified)
        new_job.save()
        return new_job

    def set_job_status(self, job, status):
        job.status = status
        job.modified = datetime.now()
        job.save()
        return job

    def update_job(self, job, status):
        self.set_job_status(job, status)
        job.modified = datetime.now()
        job.save()
        return job

    def get_job(self, job_id):
        job = Job.select().where(Job.job_id==job_id).get()
        return job

    def get_active_jobs(self):
        job_statuses = ['created', 'running', 'queued']
        jobs = Job.select().where(Job.status<<job_statuses)
        return jobs
