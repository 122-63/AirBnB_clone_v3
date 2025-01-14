#!/usr/bin/python3
""" returns a JSON: "status": "OK" """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """function return status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def count():
    """retrieves the number of each objects by type"""
    opctions = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(opctions)
