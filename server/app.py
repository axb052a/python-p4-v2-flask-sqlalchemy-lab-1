# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    # Query the database to get the earthquake with the given id
    earthquake = Earthquake.query.get(id)

    # Check if the earthquake with the given id exists
    if earthquake:
        # Format the response as a JSON string
        response_data = {
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        }
        return jsonify(response_data)
    else:
        # Return an error message if no earthquake is found
        error_message = {'message': f'Earthquake {id} not found.'}
        return make_response(jsonify(error_message), 404)

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    # Query the database to get earthquakes with a magnitude greater than or equal to the parameter value
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Format the response as a JSON string
    response_data = {
        'count': len(earthquakes),
        'quakes': [
            {
                'id': quake.id,
                'location': quake.location,
                'magnitude': quake.magnitude,
                'year': quake.year
            }
            for quake in earthquakes
        ]
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
