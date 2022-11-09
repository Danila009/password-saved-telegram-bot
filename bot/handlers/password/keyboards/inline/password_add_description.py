from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import add_description_callback


def password_add_description(password_id: int):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='add description',
                    callback_data=add_description_callback.new(password_id=password_id)
                )
            ]
        ]
    )
