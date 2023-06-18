from src.database import db

from src.database.task import Task

from datetime import datetime

class User(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    full_name       = db.Column(db.String(80), nullable=False)
    username        = db.Column(db.String(80), unique=True, nullable=False)
    role            = db.Column(db.String(10), nullable=False)
    email           = db.Column(db.String(120), unique=True, nullable=False)
    password        = db.Column(db.String(120), nullable=False)
    created_at      = db.Column(db.DateTime, default=datetime.now())
    updated_at      = db.Column(db.DateTime, onupdate=datetime.now())
    task            = db.relationship(Task, backref="user")

    def __repr__(self) -> str:
        return 'User>>>{self.username}'
