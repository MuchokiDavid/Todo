from random import choice, choices
from faker import Faker
import uuid

from models import Todo, User, db

from app import app

fake = Faker()

with app.app_context():
    print("Deleting data...................")
    User.query.delete()
    Todo.query.delete()

    print("Creating users..................")