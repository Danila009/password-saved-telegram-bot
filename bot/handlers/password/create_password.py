from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext

from bot.handlers.password.states.create_password import CreatePasswordState
from database.passwords import passwotd_data_store


async def enter_create_password(message: types.Message):
    await message.answer(text='Input title')
    await CreatePasswordState.InputTitle.set()


async def input_title(message: types.Message, state: FSMContext):
    title = message.text
    await message.answer(text='Input password')
    await state.update_data(title=title)
    await CreatePasswordState.next()


async def input_password(message: types.Message, state: FSMContext):
    password = message.text
    await message.answer(text='Input description')
    await state.update_data(password=password)
    await CreatePasswordState.next()


async def input_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    title = data.get('title')
    password = data.get('password')
    description = message.text
    try:
        await passwotd_data_store.create_password(user_id=message.from_user.id, title=title, password=password,
                                                  description=description)
        await message.answer(text='Password save!')
    except Exception as error:
        await message.reply(f'Ошибка: {error}')

    await state.finish()


def register_create_password(dp: Dispatcher):
    dp.register_message_handler(enter_create_password, commands=['create_password'])
    dp.register_message_handler(input_title, state=CreatePasswordState.InputTitle)
    dp.register_message_handler(input_password, state=CreatePasswordState.InputPassword)
    dp.register_message_handler(input_description, state=CreatePasswordState.InputDescription)
