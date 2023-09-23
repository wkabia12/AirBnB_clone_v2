#!/usr/bin/python3
"""  starts a Flask web application """

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays list of cities by states"""
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
