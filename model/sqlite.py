from peewee import SqliteDatabase, Model
from playhouse.postgres_ext import *
# db = SqliteDatabase('mysqlite.db')
db = PostgresqlExtDatabase('myapp', user='admin', password="admin")


class BaseModel(Model):

    class Meta:
        database = db
