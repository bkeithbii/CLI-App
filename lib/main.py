from peewee import *
from datetime import datetime
import sys

db = PostgresqlDatabase(
    "notesapp", user="postgres", password="", host="localhost", port=5432
)

db.connect()

# Define base model for db to be used


class BaseModel(Model):
    class Meta:
        database = db


# Define user model (will see if this works later)
class Users(BaseModel):
    first_name = CharField()
    username = CharField(unique=True)
    user_id = AutoField()


# Define notes model with properties
class Notes(BaseModel):
    title = CharField(max_length=200)
    body = TextField()
    date = CharField()
    username = ForeignKeyField(
        Users, backref="notes", field="username", on_delete="CASCADE")
    note_id = AutoField()


# Create tables for  Notes/User models
# db.drop_tables([Users])
db.create_tables([Users])
# db.drop_tables([Notes])
db.create_tables([Notes])


class Intro:
    def __init__(self):
        self.current_member = None
        self.length = 0

    # Starting option to become a member and or sign in
    def sign_in(self):
        select = input(
            "Choose a letter:\n\t [C] - Create an account\n\t [S] - Sign in\n\t [Q] - Sign out\n\t: "
        )
        if select.lower() == "C".lower():
            new_member = Member()
            self.current_member = Users(
                first_name=new_member.first_name, username=new_member.username
            )
            self.current_member.save()
            self.choices()
        elif select.lower() == "S".lower():
            username = input("Username: ")
            self.current_member = self.get_member(username)
            self.choices()
        elif select.lower() == "Q".lower():
            sys.exit()
        else:
            print("Error - Choose from the listed options")
            self.sign_in()

    # Initial menu upon members signing in
    def choices(self):
        self.length = len(self.current_member.notes)
        select = input(
            f"Welcome {self.current_member.first_name}! Pick an option:\n\t[C] - Create a note\n\t[L] - See notes library\n\t[Q] - Sign out\n\t[T] - Terminate my account\n\t[X] - Close app\n\t: "
        )
        if select.lower() == "C".lower():
            self.create_note()
        elif select.lower() == "L".lower():
            self.search_by_user()
        elif select.lower() == "Q".lower():
            self.sign_in()
        elif select.lower() == "T".lower():
            self.remove_member()
        elif select.lower() == "X".lower():
            sys.exit()
        else:
            print("Error - Choose from the listed options")
            self.choices()

    # (C)reate note functionality
    def create_note(self):
        title = input("Title: ")
        body = input("Note: ")
        new_note = Note(title, body, self.current_member.username)
        new_note.make_note()
        self.length = len(self.current_member.notes)
        print(f"{new_note.title} was added!")
        self.choices()

    # Sea(R)ch note functionality
    # Part 1 - organize notes into an array with their respective id to facilitate searching
    def search_by_user(self):
        if self.length == 0:
            print(f"{self.current_member.username} note libary is empty.")
        else:
            print(f"{self.current_member.username} notes: ")
            notes = []
            for i, note in enumerate(self.current_member.notes):
                notes.append({note.note_id})
                print(
                    f"({self.length-i})Note - Title: {note.title} - Date: {note.date}\n"
                )
            self.select_note(notes)

    # Part 2 - use the array above to find the corresponding note in the database
    def select_note(self, notes_list):
        tagged = self.length - int(input("Choose a note by its #: "))
        if tagged >= 0 and tagged < self.length:
            tagged_note = Notes.get(Notes.note_id == notes_list[tagged])
            print(
                f"\t{tagged + self.length} Note:\n\tTitle: {tagged_note.title}\n\tMessage: {tagged_note.body}\n\tDate: {tagged_note.date}\n"
            )
            self.choices()
        else:
            print("Error - search again")
            self.select_note(notes_list)

    # Check to verify member
    def get_member(self, name):
        try:
            member = Users.get(Users.username == name)
            return member
        except DoesNotExist:
            print(f"Error - Member {name} doesn't exist.")
            self.sign_in()

    # (D)elete member functionality
    def remove_member(self):
        response = input("Confirm termination of membership - Y/N: ")
        if response.lower() == "Y".lower() or "Yes".lower():
            print(
                f"Member {self.current_member.username} has been terminated.")
            self.current_member.delete_instance()
            self.sign_in()
        elif response.lower() == "N".lower() or "No".lower():
            self.choices()
        else:
            print("Error - Choose from the listed options")


# Member functionality (Member class w/ functions)
class Member:
    def __init__(self):
        self.first_name = input("First Name: ")
        self.username = self.create_username()

    def create_username(self):
        potential_username = input("Create a username: ")
        while not self.accessible(potential_username):
            potential_username = input("Please choose a different username: ")
        return potential_username

    # Only allow usernames that haven't been taken yet
    def accessible(self, name):
        taken = Users.select().where(Users.username == name)
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

        new_note = Notes(
            title=self.title,
            body=self.body,
            date=datetime.now().strftime("%c"),
            username=self.username
        )
        new_note.save()


intro = Intro()
intro.sign_in()
