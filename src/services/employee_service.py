from flask import render_template, redirect, flash, session, request
from src.database import db
from src.database.user import User
from src.database.task import Task
import validators
from werkzeug.security import generate_password_hash

url_productivity = '/dashboard/productivity/'
url_employee_detail = '/dashboard/employee-detail/'

# Fetch all data from database and display to webpage
def view_employee():
    data = User.query.all()
    if 'admin' in session:
        return render_template("employee-detail.html", data=data)
    else:
        return redirect(url_productivity)


# Delete data by id
def delete_employee(id):
    data = User.query.filter_by(id=id).first()
    task = Task.query.filter_by(user_id=data.id).first()

    if(task != ""):
        flash("Cannot delete, user is still asign to task", "success")
        return redirect( url_employee_detail )
    elif data != "":
        db.session.delete(data)
        db.session.commit()
        flash("Data deleted successfully", "success")
        return redirect( url_employee_detail )
    else :
        flash("No data found", "error")
        return redirect( url_employee_detail )


# Single data fetch
def edit_employee(id):
    data = User.query.filter_by(id=id).first()

    if data != "":
        if 'admin' in session:
            return render_template("employee-edit.html", data=data)
        else:
            return redirect( url_productivity )

    else :
        flash("No data found", "error")
        return redirect( url_employee_detail)
    

# Update data
def update_employee(id):
    data = User.query.filter_by(id=id).first()

    if data != "" and request.method == 'POST':
        data.full_name  = request.form['full_name']
        data.email      = request.form['email']
        data.username   = request.form['username']
        data.role       = request.form['role']

        db.session.commit()

        flash("Data udated successfully", "success")
        return redirect( url_employee_detail)
    else :
        flash("No data found", "error")
        return redirect( url_employee_detail )


# Insert data
def insert_employee():
    if request.method == 'POST':
        full_name   = request.form['full_name']
        username    = request.form['username']
        email       = request.form['email']
        password    = request.form['password']
        role        = request.form['role']

        if len(password) < 6:
            flash("Password must be at leat 8 characters", "error")

        elif len(username) < 3:
            flash("Username is too short", "error")

        elif not username.isalnum() or " " in username:
            flash("Username should be alphanumeric, also no spaces", "error")

        elif not validators.email(email):
            flash("Email is not valid", "error")

        elif User.query.filter_by(email=email).first() is not None:
            flash("Email is already registered, please use another email", "error")
        
        elif User.query.filter_by(username=username).first() is not None:
            flash("Username is already registered, please use another email", "error")

        else:
            pwd_hash = generate_password_hash(password)
            user = User(username=username, password=pwd_hash, email=email, full_name=full_name, role=role)
            db.session.add(user)
            db.session.commit()
            flash("Data added successfully", "success")

    if 'admin' in session:
        return render_template("employee-register.html")
    else: 
        return redirect( url_productivity )
