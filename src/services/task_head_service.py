from flask import render_template, redirect, flash, request, session
from src.database import db
from src.database.task import Task
from src.database.user import User
from src.database.project import Project

url_productivity = '/dashboard/productivity/'
url_task_head = '/dashboard/task-head/'

# Fetch all data from database and display to webpage
def view():
    # Collect data from tables
    data        = Task.query.all()
    users       = User.query.filter_by(role="user").all()
    projects    = Project.query.filter_by(status=2).all()

    if 'admin' in session:
        return render_template("task-head-detail.html", data=data, users=users, projects=projects)
    else:
        return redirect( url_productivity )


# Delete data by id
def delete(id):
    data = Task.query.filter_by(id=id).first()
   
    if data != "":
        db.session.delete(data)
        db.session.commit()
        flash("Data deleted successfully", "success")
        return redirect( url_task_head )
    else :
        flash("No data found", "error")
        return redirect( url_task_head )


# Single data fetch
def edit(id):
    # Collect data from tables
    data = Task.query.filter_by(id=id).first()
    users       = User.query.filter_by(role="user").all()
    projects    = Project.query.filter_by(status=2).all()

    if data != "":
        if 'admin' in session:
            return render_template("task-head-edit.html", data=data, users=users, projects=projects)
        else:
            return redirect( url_productivity )
    
    else :
        flash("No data found", "error")
        return redirect( url_task_head )
    

# Update data
def update(id):
    data = Task.query.filter_by(id=id).first()

    if data != "" and request.method == 'POST':
        data.project_id   = request.form['project_id']
        data.user_id      = request.form['user_id']
        data.task_name    = request.form['task_name']
        data.short_desc   = request.form['short_desc']

        db.session.commit()

        flash("Data udated successfully", "success")
        return redirect( url_task_head )
    else :
        flash("No data found", "error")
        return redirect( url_task_head )


# Insert data
def insert():
    if request.method == 'POST':
        project_id  = request.form['project_id']
        user_id     = request.form['user_id']
        task_name   = request.form['task_name']
        short_desc  = request.form['short_desc']
    
        data = Task(project_id=project_id, user_id=user_id, short_desc=short_desc, task_name=task_name)

        db.session.add(data)
        db.session.commit()
        flash("Data added successfully", "success")

    # Collect data from tables
    users       = User.query.filter_by(role="user").all()
    projects    = Project.query.filter_by(status=2).all()

    if 'admin' in session:
        return render_template("task-head-add.html", users=users, projects=projects)
    else:
        return redirect( url_productivity )
