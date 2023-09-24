#!/usr/bin/python3
"""  starts a Flask web application """

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays list of cities by states"""
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
