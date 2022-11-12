from peewee import Model, PostgresqlDatabase
from playhouse.cockroachdb import CockroachDatabase

from bot.data.config import DATABASE_URL

db = CockroachDatabase(DATABASE_URL)


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
