from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('get_passwords', 'get passwords'),
            BotCommand('create_password', 'create password'),
            BotCommand('user_info', 'get user info')
        ],
        scope=BotCommandScopeDefault()
    )
