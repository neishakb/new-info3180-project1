from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER = './app/static/uploads'

from app import views, models

app.config.from_object(__name__)

