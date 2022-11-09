import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.data.config import BOT_TOKEN
from bot.handlers.password.create_password import register_create_password
from bot.handlers.password.delete_password import register_delete_password
from bot.handlers.password.get_password import register_get_password
from bot.handlers.start_bot import register_start_bot
from bot.handlers.user.user import register_user
from bot.services.setting_commands import set_default_commands
from database.password_saved_database import create_database
from database.users.user_data_store import get_users


def register_all_handlers(dp: Dispatcher):
    register_start_bot(dp=dp)
    register_user(dp=dp)
    register_create_password(dp=dp)
    register_get_password(dp=dp)
    register_delete_password(dp=dp)


async def on_startup(dp: Dispatcher):
    create_database()
    await get_users()


async def set_all_default_commands(bot: Bot):
    await set_default_commands(bot=bot)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())

    await set_all_default_commands(bot)

    register_all_handlers(dp=dp)

    try:
        logging.basicConfig(level=logging.INFO)
        await on_startup(dp=dp)
        await dp.start_polling()
    finally:
        await bot.delete_webhook()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
