from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import add_description_callback
from bot.handlers.password.keyboards.inline.password_add_description import password_add_description
from bot.handlers.password.states.add_password_description import AddPasswordDescription
from bot.handlers.password.states.create_password import CreatePasswordState
from bot.middleware.language_middleware import ACLMiddleware
from database.passwords import passwotd_data_store


async def enter_create_password(message: types.Message):
    await message.answer(text=_('Введите заголовок ✏️'))
    await CreatePasswordState.InputTitle.set()


async def input_title(message: types.Message, state: FSMContext):
    title = message.text
    await message.answer(text=_('Введите пароль ✏️'))
    await state.update_data(title=title)
    await CreatePasswordState.next()


async def input_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    title = data.get('title')
    password = message.text

    try:
        new_password_id = await passwotd_data_store.create_password(user_id=message.from_user.id, title=title,
                                                                    password=password)
        await message.answer(text=_('Пароль сохранен!'),
                             reply_markup=password_add_description(password_id=new_password_id, _=_))
        await state.finish()
    except Exception as message:
        await message.reply(text=_('Ошибка: {}').format(message))


async def callback_description(call: types.CallbackQuery, callback_data: dict):
    global new_password_id
    new_password_id = callback_data.get('password_id')
    await call.message.answer(_('Введите описание ✏️'))
    await AddPasswordDescription.InputDescription.set()


async def input_description(message: types.Message, state: FSMContext):
    description = message.text
    try:
        await passwotd_data_store.update_description(password_id=new_password_id, description=description)
        await message.answer(text=_('Пароль обновлен!'))
        await state.finish()
    except Exception as error:
        await message.reply(text=_('Ошибка: {}').format(error))


def register_create_password(dp: Dispatcher, i18n: ACLMiddleware):
    global _
    _ = i18n.gettext

    dp.register_message_handler(enter_create_password, commands=['create_password'])
    dp.register_message_handler(input_title, state=CreatePasswordState.InputTitle)
    dp.register_message_handler(input_password, state=CreatePasswordState.InputPassword)
    dp.register_callback_query_handler(callback_description, add_description_callback.filter())
    dp.register_message_handler(input_description, state=AddPasswordDescription.InputDescription)
