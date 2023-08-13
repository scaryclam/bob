from peewee import PostgresqlDatabase

import settings


db = PostgresqlDatabase(
    settings.DATABASE['name'],
    user=settings.DATABASE['username'],
    password=settings.DATABASE['password'],
    host=settings.DATABASE['host'],
    port=settings.DATABASE['port']
)
