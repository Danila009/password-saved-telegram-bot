from aiogram.utils.callback_data import CallbackData

add_description_callback = CallbackData('add_description', "password_id")

confirmation_delete_password_callback = CallbackData('confirmation_delete_password')
delete_password_by_id_callback = CallbackData('confirmation_delete_password_by_id', 'password_id')
