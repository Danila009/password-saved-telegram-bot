from peewee import *

from database.models.base_model import BaseModel
from database.users.models.user_model import User


class Password(BaseModel):
    password_id = PrimaryKeyField('password_id')
    title = TextField(column_name='title', null=False)
    password = TextField(column_name='password', null=False)
    description = TextField(column_name='description', null=True)
    create_date = DateField(column_name='create_date', null=True)
    user = ForeignKeyField(User, column_name='user')

    class Meta:
        table_name = 'passwords'
