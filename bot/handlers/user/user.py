from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.handlers.user.keyboards.inline.callback_data.languages_callback import languages_callback
from bot.handlers.user.keyboards.inline.user_languages import languages_markup
from bot.middleware.language_middleware import ACLMiddleware
from bot.services.setting_commands import set_default_commands
from database.users import user_data_store
from database.passwords import passwotd_data_store


async def get_user(message: types.Message):
    user = await user_data_store.get_user_by_id(message.from_user.id)
    if not user:
        await message.reply(text=_('Пользователь не найден'))
    else:
        password_count = await passwotd_data_store.get_count_passwords(user_id=user.user_id)

        await message.reply(
            text=_('Имя пользователя: {}\nИмя: {}\n'
                   'Фамилия: {}\nКоличество паролей: {}').format(user.username or "-",
                                                                 user.first_name or "-",
                                                                 user.last_name or "-",
                                                                 password_count or "-"),
            reply_markup=languages_markup
        )


async def languages_update(call: types.CallbackQuery, callback_data: dict):
    language = callback_data.get('language')

    try:
        await user_data_store.update_user_language(user_id=call.from_user.id, language=language)
        await set_default_commands(bot=call.message.bot, language_code=language)
        await call.message.answer(text=_('Успешно'))
    except Exception as message:
        await call.message.reply(text=_(f'Ошибка: {message}'))


def register_user(dp: Dispatcher, i18n: ACLMiddleware):
    global _
    _ = i18n.gettext

    dp.register_message_handler(get_user, commands=['user_info'])
    dp.register_callback_query_handler(languages_update, languages_callback.filter())
