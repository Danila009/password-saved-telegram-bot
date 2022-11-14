from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from bot.data.config import I18N_DOMAIN, LOCALES_DIR

from database.users.user_data_store import get_user_by_id


async def get_lang(user_id: int):
    user = await get_user_by_id(user_id=user_id)
    if user:
        return user.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        return await get_lang(user_id=user.id) or user.locale


def setup_middleware(dp: Dispatcher):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
