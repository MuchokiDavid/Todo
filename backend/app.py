from flask import Flask, make_response, jsonify, render_template, request, session, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from functools import wraps
import uuid
import os
import datetime

from models import Todo, User, db

from dotenv import load_dotenv
load_dotenv()

app= Flask(__name__)
print(os.environ.get('SECRET_KEY'))
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

migrate= Migrate(app, db)

db.init_app(app)
api= Api(app)

@app.route('/')
def index():
    return '<h1>Welcome to our app</h1>'

class Users(Resource):
    def get(self):
        all_users= User.query.all()
        if not all_users:
            return  {'message': "No users found"}, 404
        user_dict= [user.serialize() for user in all_users]
        return make_response(jsonify({"users": user_dict}), 200)
    
    def post(self):
        data= request.get_json()
        username= data.get("username")
        email= data.get('email')
        password= data.get("password")
        hashed_password= generate_password_hash(password)
        if not username or not email or not password:
            return {"message":"Missing fields"},401
        user= User(public_id=  str(uuid.uuid4()), username= username, email=email, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User created successfully", "user_data": user.serialize()})
        except Exception as e:
            return{"message": "Error creating the user"}
        
class UserById(Resource):
    def get(self, id):
        user= User.query.get(id)
        if not user:
            return{'message':'User does not exist'},400
        user_dict= user.serialize()
        return jsonify(user_dict)
    
    def put(self, id):
        user= User.query.get(id)
        if not user:
            return{'message':'User does not exist'},400
        data = request.get_json()
        for key, value in data.items():
            setattr(user,key,value)
        db.session.commit()
        return jsonify(user.serialize())
    
    def delete(self, id):
        user= User.query.get(id)

        if not user:
            return make_response(jsonify({"message": "User not found"}), 400)
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successifully"})    

class Todos(Resource):
    def get(self):
        all_task= Todo.query.all()
        if not all_task:
            return  {'message': "No users found"}, 404
        task_dict= [task.serialize() for task in all_task]
        return make_response(jsonify({"tasks": task_dict}), 200)
    
    def post(self):
        data= request.get_json()
        category= data.get("category")
        description= data.get('description')
        complete= bool("")

        if not category or not description:
            return {"message":"Missing fields"},401
        todo= Todo(category=category, description=description, complete=complete)
        try:
            db.session.add(todo)
            db.session.commit()
            return jsonify({"message": "User created successfully", "task_data": todo.serialize()})
        except Exception as e:
            return{"message": "Error creating the user"}
        
class TodoById(Resource):
    def get(self, id):
        task= Todo.query.get(id)
        if not task:
            return{'message':'Task does not exist'},400
        task_dict= task.serialize()
        return jsonify(task_dict)
    
    def delete(self, id):
        task= Todo.query.get(id)
        if not task:
            return make_response(jsonify({"message": "Task not found"}), 400)
        db.session.delete(task)
        db.session.commit()

    def put(self, id):
        task= Todo.query.get(id)
        if not task:
            return make_response(jsonify({"message": "Task not found"}), 400)
        data = request.get_json()
        for key, value in data.items():
            setattr(task,key,value)
        db.session.commit()
        return jsonify(task.serialize())

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(Todos, '/tasks')
api.add_resource(TodoById, '/tasks/<int:id>')

if __name__=='__main__':
    app.run(port=5555, debug= True)