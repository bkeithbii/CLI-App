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
    username = ForeignKeyField(User, field="username")


# Define user model (will see if this works later)
class User(BaseModel):
    first_name = CharField()
    username = ForeignKeyField(unique=True)


# Create tables for  Notes/User models
db.create_tables([Notes])
db.create_tables([User])


# Member functionality (Member class w/ functions)
class Member:
    def __init__(self):
        self.first_name = input("First Name: ")
        self.username = 

    def create_username(self):
        potential_username = input("Create a username: ")
        while not self.available(potential_username):
            potential_username = input("Please choose a different username: ")
        return potential_username

    # Only allow usernames that haven't been taken yet
    def accessible(self, name):
        taken = User.select().where(User.username == name)
        if taken.exists():
            print(f"{name} is not available")
            return False
        else: 
            return True


db.connect()
