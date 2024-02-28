from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
import re

db= SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__= "users"

    serialize_rules= ('-todos.user',)

    id= db.Column(db.Integer, primary_key= True)
    public_id = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    todo_list= db.relationship("Todo", backref= 'user')

    @validates('email')
    def validate_email(self, key, address):
        if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", address):
            raise ValueError('Invalid Email Address')
        return address

    def __repr__(self):
        return f'<Username: {self.username}> <E-mail: {self.email}>'
    
class Todo(db.Model, SerializerMixin):
    __tablename__= "todos"
    serialize_rules= ('-user.todos')

    id = db.Column(db.Integer, primary_key=True)
    category= db.Column(db.String(50))
    text = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'<Category: {self.category}><task: {self.task}> <Status: {self.complete}>'