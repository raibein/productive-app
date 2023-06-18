from src.database import db

from datetime import datetime

class Task(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id      = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_name       = db.Column(db.String(120), nullable=False)
    short_desc      = db.Column(db.Text, nullable=True)
    start_date_time = db.Column(db.String, nullable=True)
    end_date_time   = db.Column(db.String, nullable=True)
    status          = db.Column(db.Integer, default=0)


    def __repr__(self) -> str:
        return 'Task>>>{self.task_name}'