from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import \
    confirmation_delete_password_callback

confirmation_delete_password_markup = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Confirmation',
                callback_data=confirmation_delete_password_callback.new()
            )
        ]
    ]
)