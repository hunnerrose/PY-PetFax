# This is the file where we want to initially configure Flask and write the function that will create the instance of our app. 

# 1. Import the flask package as Flask
from flask import Flask

# 2. Define a function that will be our application factory (we'll call it create_app)
def create_app():
    # 3. Create a new app instance of Flask 
    app = Flask(__name__)

    @app.route('/')
    # 4. Create a basic index route that goes to '/' and jsut returns 'Hello, PetFax!' as a string.
    def hello():
        return 'Hello, Petfax!'
    
    # Register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # Register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)
    
    return app
