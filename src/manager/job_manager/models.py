from datetime import datetime

import settings

from peewee import (
    Model, UUIDField, CharField, IntegerField, DateTimeField,
    PostgresqlDatabase)

database = PostgresqlDatabase(
    settings.DATABASES['default']['name'],
    user=settings.DATABASES['default']['user'],
    password=settings.DATABASES['default']['user'],
    host=settings.DATABASES['default']['host'],
    port=settings.DATABASES['default']['port'])


class BaseModel(Model):
    class Meta:
        database = database


class Job(BaseModel):
    job_id = UUIDField()
    name = CharField()
    status = CharField()
    harakiri_delta_seconds = IntegerField(default=30)
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'job'


database.create_tables([Job])

