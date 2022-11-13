from database.models.base_model import db
from database.passwords.models.password_model import Password
from database.users.models.user_model import User


def create_database():
    db.connect()
    db.create_tables([User, Password])
