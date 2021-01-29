#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State)
    dict_list = []
    for state in states.values():
        dict_list.append(state.to_dict())
    return jsonify(dict_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a State """
    if not request.json:
        return 'Not a json', 400
    json_data = request.json
    if 'name' not in json_data:
        return 'Missing name', 400

    new_state = State(**json_data)
    new_state.save()

    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Deletes a State object """
    states = storage.all(State)
    for state in states.values():
        if state.id == state_id:
            print(state.id)
            storage.delete(state)
            storage.save()
            return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State object """
    if not request.json:
        return 'Not a json', 400
    json_data = request.json

    state = storage.get(State, state_id)
    if not state:
        abort(404)

    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in json_data.items():
        if key not in ignored_keys:
            setattr(state, key, value)

    storage.save()
    return jsonify(state.to_dict()), 200
