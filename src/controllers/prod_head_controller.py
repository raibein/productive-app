from src import app
from src.services.prod_head_service import view, delete, edit, update, insert

url_prefix = "/dashboard/prod-head"

def prod_head_page():
    @app.route(url_prefix + '/')
    def prod_head_detail():
        return view()
    

    @app.route(url_prefix + '/delete/<int:id>')
    def prod_head_delete(id):
        return delete(id)
    

    @app.route(url_prefix + '/edit/<int:id>')
    def prod_head_edit(id):
        return edit(id)
    

    @app.route(url_prefix + '/update/<int:id>', methods=['POST', 'GET'])
    def prod_head_update(id):
        return update(id)
    
    @app.route(url_prefix + '/insert/', methods=['POST', 'GET'])
    def prod_head_insert():
        return insert()