from aiogram import types
from aiogram.dispatcher import Dispatcher

from database.passwords import passwotd_data_store


async def get_passwords(message: types.Message):
    passwords = await passwotd_data_store.get_passwords(user_id=message.from_user.id)
    password_message = ''
    for password in passwords:
        password_message = password_message + f'\ntitle: {password.title}\npassword: {password.password}\ndescription:{password.description}\n'

    await message.answer(text=password_message)


def register_get_password(dp: Dispatcher):
    dp.register_message_handler(get_passwords, commands='get_passwords')
