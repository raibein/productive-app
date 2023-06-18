from src import app
from src.services.auth_service import user_login, user_logout



'''Authentication for the User'''

def auth_page():

    '''Login by email and encrypted password'''
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        return user_login()
    

    '''Login by email and encrypted password'''
    @app.route('/logout', methods=['POST', 'GET'])
    def logout():
        return user_logout()


