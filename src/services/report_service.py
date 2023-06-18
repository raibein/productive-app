from flask import render_template, session, redirect
from src.database.user import User
from src.database.task import Task
from src.database.project import Project
import json


'''Data Collect and Display'''
def report_view():
     # Collect data from tables
    user_id     = session['admin_id']
    tasks       = Task.query.all()
    user_tasks   = Task.query.group_by('user_id').all()
    users       = User.query.filter(id!=user_id).all()
    projects    = Project.query.all()

    # Get data for Project
    arr = []
    for project in projects:
        project_name = project.project_name
        status = project.status

        dic = { 'project_name':  project_name, 'status': status }
        arr.append(dic)

    # Get data for Task
    not_started = []
    started = []
    ongoing = []
    completed = []
    left = []

    result = []

    for task in tasks:
        if task.status == 0:
            task_status = task.status
            not_started.append(task_status)

        if task.status == 1:
            task_status = task.status
            started.append(task_status)

        if task.status == 2:
            task_status = task.status
            ongoing.append(task_status)

        if task.status == 3:
            task_status = task.status
            completed.append(task_status)

        if task.status == 4:
            task_status = task.status
            left.append(task_status)

    result.append([
        { "task_status_name": "Not Started", "status": len(not_started)},
        { "task_status_name": "Started", "status": len(started)},
        { "task_status_name": "Ongoing", "status": len(ongoing)},
        { "task_status_name": "Completed", "status": len(completed)},
        { "task_status_name": "Left", "status": len(left)}
    ])

    # Get data for User
    active_user = []
    inactive_user = []
    user_result = []

    for user in users:
        for user_task in user_tasks:
            if user_task.status != 0 and user.id == user_task.user_id:
                active_user.append(user_task.status)
                # print(user_task.user_id)

            if user_task.status == 0 and user.id == user_task.user_id:
                inactive_user.append(user_task.status)
                # print(user_task.user_id)        

    user_result.append([
            {"user_status": "Active User", "status": len(active_user)},
            {"user_status": "Inactive User", "status": len(inactive_user)}
    ])
    
    # print(user_result)

    # project_cols = Project.metadata.tables['project'].columns.keys()

    if 'admin' in session:
        return render_template(
                "report.html", 
                projects=json.dumps(arr), 
                tasks=json.dumps(result), 
                users_status=json.dumps(user_result)
        )
    else:
        return redirect('/dashboard/productivity/')
