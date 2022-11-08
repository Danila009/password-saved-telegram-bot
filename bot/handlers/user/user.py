from aiogram import types
from aiogram.dispatcher import Dispatcher

from database.users import user_data_store


async def get_user(message: types.Message):
    user = await user_data_store.get_user_by_id(message.from_user.id)
    if not user:
        await message.reply(text='user not found')
    else:
        await message.reply(text=f'username: {user.username}\nfirst name: {user.first_name}\nlast name: {user.last_name}')


def register_user(dp: Dispatcher):
    dp.register_message_handler(get_user, commands=['user_info'])
