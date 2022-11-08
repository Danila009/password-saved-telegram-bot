from peewee import *

from database.models.base_model import BaseModel


class User(BaseModel):
    user_id = PrimaryKeyField(column_name='user_id')
    username = TextField(column_name='username', null=True)
    first_name = TextField(column_name='first_name', null=True)
    last_name = TextField(column_name='last_name', null=True)
    create_date = DateField(column_name='create_date', null=True)

    class Meta:
        table_name = 'users'
