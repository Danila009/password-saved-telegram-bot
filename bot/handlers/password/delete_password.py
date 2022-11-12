from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import \
    confirmation_delete_password_callback
from bot.middleware.language_middleware import ACLMiddleware
from database.passwords import passwotd_data_store

from bot.handlers.password.keyboards.inline.confirmation_delete_password import confirmation_delete_password_markup


async def confirmation_delete_passwords(message: types.Message):
    await message.answer(text=_('Удалить все пароли'), reply_markup=confirmation_delete_password_markup(_=_))


async def delete_passwords(call: types.CallbackQuery):
    try:
        await passwotd_data_store.delete_passwords()
        await call.message.reply(text=_('Успешно'))
    except Exception as error:
        await call.message.answer(text=_('Ошибка: {}').format(error))


def register_delete_password(dp: Dispatcher, i18n: ACLMiddleware):
    global _
    _ = i18n.gettext

    dp.register_message_handler(confirmation_delete_passwords, commands=['delete_passwords'])
    dp.register_callback_query_handler(delete_passwords, confirmation_delete_password_callback.filter())
