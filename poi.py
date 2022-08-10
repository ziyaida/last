# from peewee import *

# db = PostgresqlDatabase(
#     'mistery_shak',
#     host = 'localhost',
#     port = '5432',
#     user = 'dipper',
#     password = 'qwe123'
# )

# db.connect()

# class BaseModel(Model):
#     class Meta:
#         database = db

# class Bill(BaseModel):
#     name = CharField(max_length=255, null=False, unique=True)
#     skill = CharField(max_length=255, null=False)
#     age = IntegerField()
# db.create_tables([Bill])

# db.close()


