from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rvmyeeekigwzeo:60ccf2452b672b9bbe5ff2d076ad6ca8a64dac3432f73b5973de6b0f6f4f18ca@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d4io25h9cd94m2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning

db = SQLAlchemy(app)

UPLOAD_FOLDER = './app/static/uploads'

from app import views, models

app.config.from_object(__name__)

