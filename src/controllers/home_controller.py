from src import app
from src.services.home_service import home_view

def home_page():
    @app.route('/')
    def home():
        return home_view()
    
    @app.route('/dashboard/')
    def dashboard():
        return home_view()