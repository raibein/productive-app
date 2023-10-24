from src import app
from src.config.api_registers import main

main()

if __name__ == '__main__':
    
    # For Debug and Development Server
    # app.run(debug=True) # only for debuging not for production.

    # For Production Server
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)