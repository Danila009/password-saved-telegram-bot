from aiogram import Dispatcher
from aiogram.types import Message

from database.users.user_data_store import create_user


async def start_bot(message: Message):
    user = message.from_user
    await message.answer_sticker('CAACAgIAAxkBAAEGSfhjYoFIG5zGxFrkQc_oZmJ0T4snHwACcRUAAhQkyUg9cG3f7HC5TioE')
    await message.answer('Start, Bot!')

    await create_user(user_id=user.id, username=user.username, last_name=user.last_name, first_name=user.first_name)


def register_start_bot(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state='*')
