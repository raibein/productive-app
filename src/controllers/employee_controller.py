from src import app
from src.services.employee_service import view_employee, delete_employee, edit_employee, update_employee, insert_employee

url_prefix = "/dashboard/employee-detail"

def employee_page():
    @app.route(url_prefix + '/')
    def employee_detail():
        return view_employee()
    

    @app.route(url_prefix + '/delete/<int:id>')
    def delete(id):
        return delete_employee(id)
    

    @app.route(url_prefix + '/edit/<int:id>')
    def edit(id):
        return edit_employee(id)
    

    @app.route(url_prefix + '/update/<int:id>', methods=['POST', 'GET'])
    def update(id):
        return update_employee(id)
    
    @app.route(url_prefix + '/employee-register/', methods=['POST', 'GET'])
    def employee_register():
        return insert_employee()