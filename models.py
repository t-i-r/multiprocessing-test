import os
from peewee import CharField, Model, BooleanField, DateField
from playhouse.pool import PooledPostgresqlDatabase

# from app import psql_db

psql_db = PooledPostgresqlDatabase(
    database="my_database",
    host="localhost",
    port=5432,
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = psql_db
