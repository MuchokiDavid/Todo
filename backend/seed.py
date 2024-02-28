from random import choice as rc
from faker import Faker
import uuid
from werkzeug.security import check_password_hash, generate_password_hash

from models import Todo, User, db

from app import app

fake = Faker()

with app.app_context():
    print("Deleting data...................")
    User.query.delete()
    Todo.query.delete()

    print("Creating users..................")
    for i in range(20):
        fake_password= fake.password(length=8)
        hashed_password= generate_password_hash(fake_password)
        # print(hashed_password)
        user = User(public_id= str(uuid.uuid4()),username=fake.user_name(), email=fake.email(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
    print("Seeding  Users complete.................")
    
    print("Seeding tasks...............................")
    all_users= User.query.all()
    status= ["True", ""]
    for i in range(20):
        rand_user= rc(all_users)
        categories= ["Kitchen", "House", "School", "Office", "Garden", "Vacation", "Health"]
        # print(rc(status))
        new_todo= Todo(category= rc(categories), text=fake.paragraph(),complete= bool(rc(status)), user_id= rand_user.id)
        db.session.add(new_todo)
        db.session.commit()
    
    print("Seeding completed............................")
