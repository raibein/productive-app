from src.controllers.home_controller import home_page
from src.controllers.auth_controller import auth_page
from src.controllers.report_controller import report_page
from src.controllers.employee_controller import employee_page
from src.controllers.task_head_controller import task_head_page
from src.controllers.prod_head_controller import prod_head_page
from src.controllers.user_task_controller import user_task_page
from src.controllers.user_productivity_controller import productivity_page


def main():
    report_page()
    home_page()
    auth_page()
    employee_page()
    task_head_page()
    prod_head_page()
    user_task_page()
    productivity_page()