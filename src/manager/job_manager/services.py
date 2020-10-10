from uuid import uuid4

from job_manager.models import Job


class JobService:
    def create_job(self, name):
        uuid = uuid4()
        new_job = Job(
            name=name,
            job_id=uuid,
            status="created")
        new_job.save()
        return new_job

