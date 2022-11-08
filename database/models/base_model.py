from peewee import Model, SqliteDatabase

db = SqliteDatabase('password_saved_database.sqlite')


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
