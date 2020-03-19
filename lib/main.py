from peewee import *
from datetime import date

db = PostgresqlDatabase(
    "notesapp", user="postgres", password="", host="localhost", port=5432
)

# Define base model for db to be used
class BaseModel(Model):
    class Meta:
        database = db


# Define notes model with properties
class Notes(BaseModel):
    title = CharField(max_length=200)
    body = TextField()
    date = DateField()


db.connect()
