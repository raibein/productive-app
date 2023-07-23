from src import app
from src.api_registers import main


if __name__ == '__main__':
    main()
    # app.run(debug=True) # only for debuging not for production.
    app.run(debug=False)
