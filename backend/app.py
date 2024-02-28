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
        

    

api.add_resource(Users, '/users')

if __name__=='__main__':
    app.run(port=5555, debug= True)