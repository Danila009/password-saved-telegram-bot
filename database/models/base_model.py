from peewee import Model, PostgresqlDatabase

db = PostgresqlDatabase(
    'das9gsd3v0jmmq',
    user='tqjgvatigefhyi',
    password='d1d8c51c3b76eb5d623f8bfee3ff65424c0725ee0b0b1fca598f394a747aaf92',
    host='ec2-100-26-39-41.compute-1.amazonaws.com',
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = db
        order_by = 'id'
