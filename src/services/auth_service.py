from flask import request, flash, session, redirect
from werkzeug.security import check_password_hash

from src.database.user import User



'''Login by email and encrypted password'''
def user_login():

    if request.method == 'POST':
        username    = request.form['username']
        password    = request.form['password']
        
        data = User.query.filter_by(username=username).first()

        if data != "":
            is_pass_correct = check_password_hash(data.password, password)

            if is_pass_correct:
                if data.role == 'user':
                    session['user']         = data.username
                    session['user_email']   = data.email
                    session['user_id']      = data.id
                    session['user_role']    = data.role
                    flash("The user "+data.full_name+" logged in successfully", "success")
                    return redirect ('/dashboard/productivity/')

                elif data.role == 'admin':
                    session['admin']        = data.username
                    session['admin_email']  = data.email
                    session['admin_id']     = data.id
                    session['admin_role']   = data.role
                    flash("The user "+data.full_name+" logged in successfully", "success")
                    return redirect ('/dashboard/report/')
                
            else :
                flash("Wrong credentials, please try again", "error")
                return redirect("/")

        else:
            flash("Someting wrong, please try again", "error")
            return redirect("/")


# Log out
def user_logout():
    if 'user' in session:
        session.pop('user', None)
        session.pop('user_email', None)
        session.pop('user_id', None)
        session.pop('user_role', None)
    else:
        session.pop('admin', None)
        session.pop('admin_email', None)
        session.pop('admin_id', None)
        session.pop('admin_role', None)

    flash("You are logout successfully", "success")
    return redirect("/")