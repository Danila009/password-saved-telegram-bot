from aiogram import Dispatcher
from aiogram import types

from bot.middleware.language_middleware import ACLMiddleware
from database.users.user_data_store import create_user


async def start_bot(message: types.Message):
    user = message.from_user
    await message.answer_sticker('CAACAgIAAxkBAAEGSfhjYoFIG5zGxFrkQc_oZmJ0T4snHwACcRUAAhQkyUg9cG3f7HC5TioE')
    await message.answer(_('Привет, {}!').format(user.username or user.first_name or user.last_name))

    await create_user(
        user_id=user.id, username=user.username,
        last_name=user.last_name, first_name=user.first_name
    )


def register_start_bot(dp: Dispatcher, i18n: ACLMiddleware):
    global _
    _ = i18n.gettext

    dp.register_message_handler(start_bot, commands=['start'], state='*')
