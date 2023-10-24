from flask import Flask
import os

from src.database.user import User
from src.database.project import Project
from src.database.task import Task

from dotenv import load_dotenv

from src.database import db


# Imports Autoload the Environment Variable
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = ROOT_DIR + "/../"
load_dotenv(os.path.join(path, '.env'))


config = None

app = Flask(__name__, instance_relative_config=True)

if config is None:
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
else:
    app.config.from_mapping(config)


'''
db.app = app
db.init_app(app)
app.app_context().push()
db.create_all()
'''
db.init_app(app)
app.app_context().push()
# db.create_all() # Uncommented this line only to create database with new tables during the running the application
