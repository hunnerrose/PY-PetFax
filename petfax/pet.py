# 1. Import the Blueprint class
from flask import ( Blueprint, render_template )

# 4. Import json
import json

# 5. open() the pets.json file by passing it an argument. Pass the entire open function as an argument to json.load(). Save this decoded JSON to a variable named pets.
pets = json.load(open('pets.json'))
print(pets)

# 2. Instantiate the blueprint
bp = Blueprint('pet', __name__, url_prefix='/pets')

# 3. Index route
@bp.route('/')
def index(): 
                # 6. In the index method, pass the render_template a 2nd argument; name it pets and pass it the pets variable that we just loaded with data. This way, in the index.html, we can loop through the data using the pets variable.
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)
