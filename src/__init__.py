from flask import Flask
import os

from src.database.user import User
from src.database.project import Project
from src.database.task import Task

from src.database import db


test_config = None

app = Flask(__name__, instance_relative_config=True)

if test_config is None:
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
else:
    app.config.from_mapping(test_config)


'''
db.app = app
db.init_app(app)
app.app_context().push()
db.create_all()
'''
db.init_app(app)
app.app_context().push()
# db.create_all() # Uncommented this line only to create database with new tables during the running the application