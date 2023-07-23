# Flask Developer Productive Application

## Pre-requisite
1. Install `pip`
2. Install `python`

## Add to environment file (.env) file
`add this two lines to .env file`
1. export SECRET_KEY="<Any_Secret_Key>"
2. export SQLALCHEMY_DB_URI="sqlite:///data.db"

## Create the virtual environment
1. Command : python3 -m venv venv

## Enable virtual environment (in linux env)
1. Command : source ./venv/bin/activate
`or`
1. Command : source ./venv/Scripts/activate

## Disable virtual environment (in linux env)
1. Command : deactivate

## Install `requirements.txt`
1. Command : pip install -r requirements.txt

## Run appliction
1. Command : python app.py

## Description and use of the Application

## Login Detail
There are two types or roles of the users to login one is for the admin user and another is the only users.

For the admin ->
`username : administrator`
`password : administrator`

For the user -> Login to the admin dashboard -> go to the `Empoloyee Detail` Find out and user -> username
`username and password are same`

## Application Detail
There are the two different users one is the admin and another is the employee. The application use the common 
dashboard for both types of users but only depends on who logged and get the authenticate.

The concept here is for the admin is to create the Projects, Tasks and New Employees. After creating the project, 
the project must be ongoing, i.e processing state, so the task can create also the user can assign for this task.
That means, in the applicaiton `Employee Detail`, `Project Head`, and `Task Head` are the creation, update, delete, 
and get the list and status of the per head. The delete of employee and project cannot be possible if those are
assign to the task. Also the edit and delete are disabled if the tasks are completed state.

The employee can start the task and as per the task going on they can also update as ongoing state and finally 
completed state. So the can will close. But they can also left the task if they could not handle it and by admin
the task can reassign to another employee.

The report will generate employee working progress and task completion. Also there is the project base report.

## Update Application (follow up new version)
The application can also changes various way to improve. In the users perspective they can only have their own username 
and password who provided them by the admin. This should be change as the user must change their password by themself or 
have to authenticate to create their own username and password. There is also missing the team for the group of the users. 
This can also build with team like developers, qa, managers and so on. The task can also be reopen if there are the bugs 
in them and this task can review from the admin or leas. The sharing dashboard can be seperated. Tracking the change even 
by admin rights who has changed for example to assign the different user for the task. Add the pagination  if the list 
is going too long. The reports are also need to generate more for example to create the charts of per projects status, 
individual user's progressing stat, duration of completing each task detail, the percentage of capacity of the user 
to complete the task and so on.

## Understanding of Problem
Try to understand the problem before start any project. Research and collect the ideas. Pointing and list them all. Roadmap 
on those ideas. Then start to build them. During building the application I have been correcting and improving them for 
example the table structure. The different dashboard to the role base users. The visualization of ther users and the admin.

## Interesting Facts
During developing the appliction interesting fact is the code structure using the MVC pattern and scale the application, also easy 
to correction. Another interesting thing is the chart.js applicable. First using the data passing indiviudally, also convert data 
to the `count` in `jinja template` which can be seen in `productivity.html` file. after that sending thd data into json format. Javascript adopt the json data, separated the labal and data then simply display it into the brower. The various type of data 
visualizatioin or chart can be found in chart.js all in one.

It's the time consuming to create the frontend and backend so simply using the role separated, each user role type get their own 
dashboard and implement their job to be done. Also there are the separated nav buttons depends on the user roles.

Also in the creating the task, it can be separated and assign the task to the user but during the creating the task the user can
assign the task which also save time and effor I felt duing the building the application.


# Deploy on Heroku


## Pre-requisite
`For macbook to install heroku cli`
1. brew tap heroku/brew && brew install heroku

## Login to Heroku
1. heroku login

## If the project is not created, create the project in Heroku
1. heroku create <app_name>
`eg: heroku create productive-app`

## Deploy code to Heroku by git
1. git push heroku <branch_name>
`eg: git push heroku main`

## Open add from Heroku
1. command: heroku open

## Get logs from Heroku
1. command: heroku logs --tail