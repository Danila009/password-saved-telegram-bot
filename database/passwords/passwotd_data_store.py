from database.passwords.models.password_model import Password
from database.users.models.user_model import User


async def create_password(user_id: int, title: str, password: str, description: str = None):
    user = User.get_by_id(user_id)
    if user:
        new_password = Password.create(user=user, title=title, password=password, description=description)
        return new_password.password_id


async def update_description(password_id: int, description: str):
    qry = Password.update({Password.description: description}).where(Password.password_id == password_id)
    qry.execute()


async def get_passwords(user_id: int, search: str = None):
    if search:
        return Password.select().where(
            Password.user == user_id and (
                    Password.title.contains(search)
                    or Password.description.contains(search)
                    or Password.password.contains(search)
            ))
    else:
        return Password.select().where(Password.user == user_id)


async def get_count_passwords(user_id: int):
    return Password.select().where(Password.user == user_id).count()


async def delete_password(password_id: int):
    qry = Password.delete_by_id(password_id)
    qry.execute()


async def delete_passwords():
    qry = Password.delete()
    qry.execute()
