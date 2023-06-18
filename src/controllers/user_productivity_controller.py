from src import app
from src.services.productivity_service import view

url_prefix = "/dashboard"

def productivity_page():
    @app.route(url_prefix + '/productivity/')
    def productivity_detail():
        return view()