from peewee import Model, CharField

from database import db


class JobConfig(Model):
    name = CharField()
    schedule = CharField()
    message = CharField()

    class Meta:
        database = db


def setup_models():
    db.connect()
    db.create_tables([JobConfig])
