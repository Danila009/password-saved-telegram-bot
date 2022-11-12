from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from bot.data.config import CHAT_ID


async def set_default_commands(bot: Bot, chat_id: int = CHAT_ID, language_code: str = None):
    DEFAULT_COMMANDS = {
        'ru': [
            BotCommand('get_passwords', 'получить пароли'),
            BotCommand('get_passwords_file', 'получить файл с паролями'),
            # BotCommand('get_passwords_table', 'получить таблицу паролей'),
            BotCommand('create_password', 'создать пароль'),
            BotCommand('delete_passwords', 'удалите все пароли'),
            BotCommand('user_info', 'получить информацию о пользователе')
        ],
        'en': [
            BotCommand('get_passwords', 'get passwords'),
            BotCommand('get_passwords_file', 'get a file with passwords'),
            # BotCommand('get_passwords_table', 'get passwords table'),
            BotCommand('create_password', 'create password'),
            BotCommand('delete_passwords', 'delete all passwords'),
            BotCommand('user_info', 'get user info')
        ]
    }

    if language_code:
        for code, commands in DEFAULT_COMMANDS.items():
            await bot.delete_my_commands(
                language_code=code,
                scope=BotCommandScopeChat(chat_id)
            )

        await bot.set_my_commands(
            commands=DEFAULT_COMMANDS.get(language_code),
            scope=BotCommandScopeChat(chat_id)
        )
    else:
        for code, commands in DEFAULT_COMMANDS.items():
            await bot.set_my_commands(
                language_code=code,
                commands=commands,
                scope=BotCommandScopeChat(chat_id)
            )
