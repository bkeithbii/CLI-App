from peewee import *
from datetime import date

db = PostgresqlDatabase(
    "notesapp", user="postgres", password="", host="localhost", port=5432
)


db.connect()
