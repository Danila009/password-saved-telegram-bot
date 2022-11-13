import os
import xlwt

from aiogram import types
from aiogram.dispatcher import Dispatcher

from prettytable import PrettyTable

from bot.handlers.password.keyboards.inline.callback_data.inline_callback_data import \
    delete_password_by_id_callback
from bot.handlers.password.keyboards.inline.confirmation_delete_password import \
    delete_password_by_id_markup
from bot.middleware.language_middleware import ACLMiddleware
from database.passwords import passwotd_data_store


async def get_passwords(message: types.Message):
    search = message.get_args()
    passwords = await passwotd_data_store.get_passwords(user_id=message.from_user.id, search=search)

    if passwords:
        for password in passwords:
            await message.answer(
                text=_('\nЗаголовок: {}\n'
                       'Пароль: {}\nОписание:{}\n').format(
                    password.title, password.password, password.description or "-"
                ),
                reply_markup=delete_password_by_id_markup(password_id=password.password_id, _=_)
            )
    else:
        await message.answer_sticker('CAACAgIAAxkBAAEGYn1jbmOJKO5-ktHqV-l0Qs_O2kaHfQAC3gUAAj-VzApvED_5xd0MFysE')


async def get_passwords_table(message: types.Message):
    search = message.get_args()
    passwords = await passwotd_data_store.get_passwords(user_id=message.from_user.id, search=search)

    if passwords:
        table = PrettyTable()
        table.field_names = [_('Заголовок'), _('Пароль'), _('Описание')]

        for password in passwords:
            table.add_row([password.title, password.password, password.description or '-'])

        await message.answer(text=table.get_string())
        print(table)
    else:
        await message.answer_sticker('CAACAgIAAxkBAAEGYn1jbmOJKO5-ktHqV-l0Qs_O2kaHfQAC3gUAAj-VzApvED_5xd0MFysE')


async def delete_password_by_id(call: types.CallbackQuery, callback_data: dict):
    password_id = callback_data.get('password_id')

    await passwotd_data_store.delete_password(password_id=password_id)
    await call.message.answer(text=_('Успешно'))


async def get_passwords_file(message: types.Message):
    search = message.get_args()
    passwords = await passwotd_data_store.get_passwords(user_id=message.from_user.id, search=search)

    if passwords:
        main_text_font = xlwt.Font()
        main_text_font.name = 'Times New Roman'
        main_text_font.bold = True

        main_text_style = xlwt.XFStyle()
        main_text_style.font = main_text_font

        text_font = xlwt.Font()
        text_font.name = 'Times New Roman'

        text_style = xlwt.XFStyle()
        text_style.font = text_font

        wb = xlwt.Workbook()
        ws = wb.add_sheet(_('Основной лист'))
        ws.write(0, 0, _('идентификатор пароля'), main_text_style)
        ws.write(0, 1, _('Заголовок'), main_text_style)
        ws.write(0, 2, _('Пароль'), main_text_style)
        ws.write(0, 3, _('Описание'), main_text_style)
        ws.write(0, 4, _('дата создания'), main_text_style)
        ws.write(0, 5, _('идентификатор пользователя'), main_text_style)

        for index, password in enumerate(passwords):
            ws.write(index + 1, 0, password.password_id, text_style)
            ws.write(index + 1, 1, password.title, text_style)
            ws.write(index + 1, 2, password.password, text_style)
            ws.write(index + 1, 3, password.description or "-", text_style)
            ws.write(index + 1, 4, password.create_date, text_style)
            ws.write(index + 1, 5, password.user.user_id, text_style)

        wb.save('passwords_file.xls')
        await message.answer_document(types.InputFile('passwords_file.xls'))
        os.remove("passwords_file.xls")
    else:
        await message.answer_sticker('CAACAgIAAxkBAAEGYn1jbmOJKO5-ktHqV-l0Qs_O2kaHfQAC3gUAAj-VzApvED_5xd0MFysE')


def register_get_password(dp: Dispatcher, i18n: ACLMiddleware):
    global _
    _ = i18n.gettext

    dp.register_message_handler(get_passwords, commands='get_passwords')
    dp.register_message_handler(get_passwords_file, commands='get_passwords_file')
    dp.register_message_handler(get_passwords_table, commands='get_passwords_table')

    dp.register_callback_query_handler(delete_password_by_id, delete_password_by_id_callback.filter())
