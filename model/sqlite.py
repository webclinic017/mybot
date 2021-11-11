from peewee import SqliteDatabase, Model
db = SqliteDatabase('mysqlite.db')


class BaseModel(Model):

    class Meta:
        database = db
