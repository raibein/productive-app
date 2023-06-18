from flask import request, render_template, session, redirect

'''Data Collect, Display and Redirect'''
def home_view():
    if not 'user' in session:
        if 'admin' in session:
            return redirect("/dashboard/report/")
        return render_template("login.html")

    if not 'admin' in session:
        if 'user' in session:
            return redirect("/dashboard/productivity/")
        return render_template("login.html")
