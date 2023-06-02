
                    # TERMINAL: Before creating Flask app, create a virtual environment by running commands 'python3 -m venv venv' and '. venv/scripts/activate' in the terminal 
# 1. Configure Flask (similar to Express in React)
from flask import Flask
app = Flask(__name__)

# 2. Create a route to call on the app instance. Be sure to put the @ sign in front! The @ denotes the use of a decorator, which is a function that extends the functionality of an existing function.
@app.route('/')
# 3. Tell the route what to do when that endpoint is used by defining a method directly underneath
def index():
    return 'Hello, this is PetFax!'
                    # TERMINAL: To run this Flask application, in the terminal we'd run the command 'flask run' (similar to npm run with Node.js apps). With Flask, we don't need to specify a PORT to run it on since it defaults to Port 5000. To make Flask automatically restart when a file has been changed, run 'flask run --reload'

@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'
    