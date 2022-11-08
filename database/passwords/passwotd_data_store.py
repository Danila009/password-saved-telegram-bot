from database.passwords.models.password_model import Password
from database.users.models.user_model import User


async def create_password(user_id: int, title: str, password: str, description: str):
    user = User.get_by_id(user_id)
    if user:
        Password.create(user=user, title=title, password=password, description=description)


async def get_passwords(search: str = None):
    Password.get()


async def delete_password(password_id: int):
    Password.delete_by_id(password_id)


async def delete_passwords():
    Password.delete()
