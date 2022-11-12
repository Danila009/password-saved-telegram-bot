from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import \
    confirmation_delete_password_callback, delete_password_by_id_callback


def confirmation_delete_password_markup(_):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=_('Подтвердите ❗️'),
                    callback_data=confirmation_delete_password_callback.new()
                )
            ]
        ]
    )


def delete_password_by_id_markup(password_id: int, _):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=_('Удалить пароль 🗑'),
                    callback_data=delete_password_by_id_callback.new(password_id=password_id)
                )
            ]
        ]
    )
