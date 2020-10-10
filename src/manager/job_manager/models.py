from datetime import datetime

from peewee import (
    Model, UUIDField, CharField, IntegerField, DateTimeField,
    PostgresqlDatabase)

database = PostgresqlDatabase(
    'manager', 
    user='vagrant', 
    password='vagrant',
    host='127.0.0.1', 
    port=5432)


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

