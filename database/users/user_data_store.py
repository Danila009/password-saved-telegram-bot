from database.users.models.user_model import User


async def create_user(user_id: int, username: str, last_name: str, first_name: str):
    user = User.get_or_none(User.user_id == user_id)
    if not user:
        User.create(user_id=user_id, username=username, last_name=last_name, first_name=first_name)


async def get_user_by_id(user_id: int):
    user = User.get_or_none(User.user_id == user_id)
    return user


async def get_users():
    for user in User.select():
        print(str(user.username))
