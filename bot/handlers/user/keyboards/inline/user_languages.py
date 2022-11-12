from aiogram import types

from bot.handlers.user.keyboards.inline.callback_data.languages_callback import languages_callback

languages_markup = types.InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text='Русский 🇷🇺',
                callback_data=languages_callback.new(language='ru')
            ),
            types.InlineKeyboardButton(
                text='English 🇬🇧',
                callback_data=languages_callback.new(language='en')
            )
        ]
    ]
)