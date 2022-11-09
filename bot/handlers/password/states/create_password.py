from aiogram.dispatcher.filters.state import StatesGroup, State


class CreatePasswordState(StatesGroup):
    InputTitle = State()
    InputPassword = State()
