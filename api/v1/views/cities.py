#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def list_cities(state_id):
    """ Retrieves the list of all City objects of a State """
    state = storage.get(State, state_id)
    dict_list = []
    if not state:
        abort(404)
    for city in state.cities:
        dict_list.append(city.to_dict())
    return jsonify(dict_list)
