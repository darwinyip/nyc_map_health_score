import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.url import URL
from config import DATABASE

app = Flask(__name__, static_folder="../static/build/static", template_folder="../static/build")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL(**DATABASE)
db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))


from app import views