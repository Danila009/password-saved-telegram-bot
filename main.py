import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.data.config import BOT_TOKEN
from bot.handlers.errors.errors_handler import register_errors_handler
from bot.handlers.password.create_password import register_create_password
from bot.handlers.password.delete_password import register_delete_password
from bot.handlers.password.get_password import register_get_password
from bot.handlers.start_bot import register_start_bot
from bot.handlers.user.user import register_user
from bot.middleware.language_middleware import setup_middleware
from bot.services.setting_commands import set_default_commands
from database.password_saved_database import create_database
from database.users.user_data_store import get_users

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())

i18n = setup_middleware(dp=dp)


async def task():
    while True:
        # await bot.send_message(text='task test', chat_id=CHAT_ID)
        print('test task')
        await asyncio.sleep(21600)


def register_all_handlers():
    register_start_bot(dp=dp, i18n=i18n)

    register_user(dp=dp, i18n=i18n)

    register_create_password(dp=dp, i18n=i18n)
    register_get_password(dp=dp, i18n=i18n)
    register_delete_password(dp=dp, i18n=i18n)

    register_errors_handler(dp=dp, i18n=i18n)


async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(task())

    create_database()
    await get_users()


async def set_all_default_commands():
    await set_default_commands(bot=bot)


async def main():
    try:
        logging.basicConfig(level=logging.INFO)

        await set_all_default_commands()
        register_all_handlers()

        await on_startup()
        await dp.start_polling()

        await bot.get_webhook_info()
    finally:
        await bot.delete_webhook()
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
