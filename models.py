from peewee import *
from app import psql_db


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = psql_db
