from src import app
from src.services.report_service import report_view

url_prefix = "/dashboard"

def report_page():
    @app.route(url_prefix + '/report/')
    def report():
        return report_view()