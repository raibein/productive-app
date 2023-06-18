from flask import render_template, redirect, flash, request, session
from src.database import db
from src.database.project import Project
from src.database.task import Task

url_productivity = '/dashboard/productivity/'
url_prod_head = '/dashboard/prod-head/'


# Fetch all data from database and display to webpage
def view():
    data = Project.query.all()
    if 'admin' in session:
        return render_template("prod-head-detail.html", data=data)
    else:
        return redirect( url_productivity )


# Delete data by id
def delete(id):
    data = Project.query.filter_by(id=id).first()
    task = Task.query.filter_by(project_id=data.id).first()

    if(task != ""):
        flash("Cannot delete, it is still using to task", "success")
        return redirect( url_prod_head )
    elif data != "":
        db.session.delete(data)
        db.session.commit()
        flash("Data deleted successfully", "success")
        return redirect( url_prod_head )
    else :
        flash("No data found", "error")
        return redirect( url_prod_head )


# Single data fetch
def edit(id):
    data = Project.query.filter_by(id=id).first()

    if data != "":
        if 'admin' in session:
            return render_template("prod-head-edit.html", data=data)
        else:
            return redirect( url_productivity )
    
    else :
        flash("No data found", "error")
        return redirect( url_prod_head )
    

# Update data
def update(id):
    data = Project.query.filter_by(id=id).first()

    if data != "" and request.method == 'POST':
        data.project_name   = request.form['project_name']
        data.short_desc     = request.form['short_desc']
        data.start_date     = request.form['start_date']
        data.end_date       = request.form['end_date']
        data.status         = request.form['status']

        db.session.commit()

        flash("Data udated successfully", "success")
        return redirect( url_prod_head )
    else :
        flash("No data found", "error")
        return redirect( url_prod_head )


# Insert data
def insert():
    if request.method == 'POST':
        project_name    = request.form['project_name']
        short_desc      = request.form['short_desc']
        start_date      = request.form['start_date']
        end_date        = request.form['end_date']
        status          = request.form['status']
    
        data = Project(project_name=project_name, short_desc=short_desc, start_date=start_date, end_date=end_date, status=status)
        db.session.add(data)
        db.session.commit()
        flash("Data added successfully", "success")


    if 'admin' in session:
        return render_template("prod-head-add.html")
    else:
        return redirect( url_productivity )
