from flask import request, render_template, flash, session, redirect
from src.database.task import Task
from src.database.user import User
from src.database.project import Project
import json


'''Data Collect and Display'''
def view():
    # Collect data from tables
    user_id     = session['user_id']
    data        = Task.query.filter_by(user_id=user_id).all()
    users       = User.query.filter_by(id=user_id).all()
    projects    = Project.query.filter_by(status=2).all()
   
    testObj = [ 15,25,10,22,22]
    
    notstarted  = Task.query.filter_by(user_id=user_id, status=0).all()
    started     = Task.query.filter_by(user_id=user_id, status=1).all()
    ongoing     = Task.query.filter_by(user_id=user_id, status=2).all()
    completed   = Task.query.filter_by(user_id=user_id, status=3).all()
    left        = Task.query.filter_by(user_id=user_id, status=4).all()



    if 'user' in session:
        return render_template("productivity.html", 
            data=data, 
            users=users, 
            projects=projects,
            notstarted=notstarted, 
            started=started, 
            ongoing=ongoing, 
            completed=completed, 
            left=left,
            testObj=json.dumps(testObj)
        )
    else:
        return redirect('/dashboard/productivity/')