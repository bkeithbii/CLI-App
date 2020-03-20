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



class Intro:
    def __init__(self):
        self.current_member = None
        self.length = 0
    
    # Starting option to become a member and or sign in
    def sign_in(self):
        select = input(
            "Choose a letter:\n\t[C] - Create an account\n\t[S] - Sign in\n\t[Q] - Sign out\n\t")
        if select.lower() == "C":
            new_member = Member()
            self.current_member = User(
                first_name=new_member.first_name, username=new_member.username
            )
            self.current_member.save()
            self.choices()
        elif select.lower() == "S": 
            username = input("Username: ")
            self.current_member = self.get_member(username)
            self.choices()
        elif select.lower() == "Q":
            sys.exit()
        else:
            print("Error - Choose from the listed options")
            self.sign_in()

    def choices(self):
        self.length = len(self.current_member.notes)
        select = input(f"Welcome {self.current_member.first_name}! 
        Pick an option:\n\t[C] - Create a note\n\t[L] - See notes library\n\t[Q] - Sign out\n\t[T] - Terminate my account\n\t[X] - Close app\n\t")
        if select == "C":
            self.create_note()
        elif select == "L":
            self.search_by_user()
        elif select == "Q":
            self.sign_in()
        elif select == "T":
            self.remove_member()
        elif select == "X":
            sys.exit()
        else:
            print("Error - Choose from the listed options")
            self.choices()


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

# Note functionality (Note class w/ functions)
class Note: 
    def __init__(self, title, body, member):
        self.title = title
        self.body = body
        self.username = member

    def make_note(self):
        new_note = Note(title=self.title, body=self.body, date=date.now().strftime(), username=self.username)
        new_note.save()

db.connect()
