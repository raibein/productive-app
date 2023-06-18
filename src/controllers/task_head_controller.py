from src import app
from src.services.task_head_service import view, delete, edit, update, insert

url_prefix = "/dashboard/task-head"

def task_head_page():
    @app.route(url_prefix + '/')
    def task_head_detail():
        return view()
    

    @app.route(url_prefix + '/delete/<int:id>')
    def task_head_delete(id):
        return delete(id)
    

    @app.route(url_prefix + '/edit/<int:id>')
    def task_head_edit(id):
        return edit(id)
    

    @app.route(url_prefix + '/update/<int:id>', methods=['POST', 'GET'])
    def task_head_update(id):
        return update(id)
    
    @app.route(url_prefix + '/insert/', methods=['POST', 'GET'])
    def task_head_insert():
        return insert()