from flask import Flask, make_response, jsonify, render_template, request, session, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from functools import wraps
import os
import datetime

from models import Todo, User, db

from dotenv import load_dotenv
load_dotenv()

app= Flask(__name__)
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

migrate= Migrate(app, db)

db.init_app(app)
api= Api(app)