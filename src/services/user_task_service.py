from flask import render_template, redirect, flash, request, session
from src.database import db
from src.database.task import Task
from src.database.user import User
from src.database.project import Project

url_report = '/dashboard/report/'
url_user_task = '/dashboard/user-task-manage/'

# Fetch all data from database and display to webpage
def view():
    # Collect data from tables
    user_id     = session['user_id']
    data        = Task.query.filter_by(user_id=user_id).all()
    users       = User.query.filter_by(id=user_id).all()
    projects    = Project.query.filter_by(status=2).all()

    if 'user' in session:
        return render_template("user-task-detail.html", data=data, users=users, projects=projects)
    else:
        return redirect( url_report )



# Single data fetch
def edit(id):
    # Collect data from tables
    data = Task.query.filter_by(id=id).first()
    users       = User.query.filter_by(role="user").all()
    projects    = Project.query.filter_by(status=2).all()

    if data != "":
        if 'user' in session:
            return render_template("user-task-edit.html", data=data, users=users, projects=projects)
        else:
            return redirect( url_report )
    
    else :
        flash("No data found", "error")
        return redirect( url_user_task )
    

# Update data
def update(id):
    data = Task.query.filter_by(id=id).first()

    if data != "" and request.method == 'POST':
        data.project_id         = request.form['project_id']
        data.user_id            = session['user_id']
        data.task_name          = request.form['task_name']
        data.short_desc         = request.form['short_desc']
        data.status             = request.form['status']
        data.start_date_time    = request.form['start_date']
        data.end_date_time      = request.form['end_date']

        db.session.commit()

        flash("Data udated successfully", "success")
        return redirect( url_user_task )
    else :
        flash("No data found", "error")
        return redirect( url_user_task )