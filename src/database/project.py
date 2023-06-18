from src.database import db

from src.database.task import Task

from datetime import datetime

class Project(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    project_name    = db.Column(db.String(120), nullable=False)
    short_desc      = db.Column(db.Text, nullable=True)    
    start_date      = db.Column(db.String(40), nullable=True)
    end_date        = db.Column(db.String(40), nullable=True)
    status          = db.Column(db.Integer, default=0)
    task            = db.relationship(Task, backref="project")


    def __repr__(self) -> str:
        return 'Project>>>{self.task_name}'
