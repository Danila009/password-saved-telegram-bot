from peewee import Model
from playhouse.db_url import connect

from bot.data.config import DATABASE_URL

db = connect(DATABASE_URL)


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
