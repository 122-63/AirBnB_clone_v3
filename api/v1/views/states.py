#!/usr/bin/python3
"""Retrieve an object into a valid JSON"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State

@app_views.route('/states', strict_slashes=False, methods=['GET'])
def all_state():
    """ list of all State objects:"""
    states = storage.all("State").values()
    list_states = []
    for state in states:
        data = state.to_dict()
        list_states.append(data)
    return jsonify(list_states)

@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def states_with_id(state_id):
    """Returns an empty dictionary with the status code 200"""
    states = storage.all("State").values()
    for state in states:
        if state.id == state_id:
            linked = state.to_dict()
            return jsonify(linked)
    abort(404)

@app_views.route('/states/<state_id>', strict_slashes=False, methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object"""
    states = storage.all("State").values()
    for state in states:
        if state.id == state_id:
            storage.delete(state)
            storage.save()
            return jsonify({}), 200
    abort(404)

@app_views.route('/states', strict_slashes=False, methods=['POST'])
def post_state():
    """Creates a State"""
    if not request.is_json:
        abort(404, description="Not a JSON")

    request_data = request.get_json()
    if request_data.get('name') is None:
        abort(404, description="Missing name")

    obj_state = State(**request_data)
    storage.new(obj_state)
    storage.save()

    return jsonify(obj_state.to_dict()), 201

@app_views.route('/states/<state_id>', strict_slashes=False, methods=['PUT'])
def put_state(state_id):
    """Updates a State object"""
    if not request.is_json:
        abort(404, description="Not a JSON")






