#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def list_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State)
    dict_list = []
    for state in states.values():
        dict_list.append(state.to_dict())
    return jsonify(dict_list)


