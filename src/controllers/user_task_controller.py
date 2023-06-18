from src import app
from src.services.user_task_service import view, edit, update

url_prefix = "/dashboard/user-task-manage"

def user_task_page():
    @app.route(url_prefix + '/')
    def user_task_detail():
        return view()


    @app.route(url_prefix + '/edit/<int:id>')
    def user_task_edit(id):
        return edit(id)
    

    @app.route(url_prefix + '/update/<int:id>', methods=['POST', 'GET'])
    def user_task_update(id):
        return update(id)