from peewee import Model, MySQLDatabase

db = MySQLDatabase(
    database='ISPr24-39_BeluakovDS_Password_Saved_Telegram_Bot',
    user='ISPr24-39_BeluakovDS',
    password='ISPr24-39_BeluakovDS',
    host='cfif31.ru',
    port=3306,
    charset='utf8'
)


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
