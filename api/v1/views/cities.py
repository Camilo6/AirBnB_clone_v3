#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import jsonify, abort, request


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


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """ Retrieves a City object """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """ Creates a City """
    state = storage.get(State, state_id)
    if not request.json:
        return 'Not a JSON', 400
    json_data = request.json
    if 'name' not in json_data:
        return 'Missing name', 400
    if not state:
        abort(404)

    json_data['state_id'] = state_id
    new_city = City(**json_data)
    new_city.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ Updates a City object """
    if not request.json:
        return 'Not a JSON', 400
    json_data = request.json

    city = storage.get(City, city_id)
    if not city:
        abort(404)

    ignored_keys = ['id', 'created_at', 'updated_at', 'state_id']
    for key, value in json_data.items():
        if key not in ignored_keys:
            setattr(city, key, value)

    storage.save()
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """ Deletes a City object """
    cities = storage.all(City).values()
    for city in cities:
        if city.id == city_id:
            print(city.id)
            storage.delete(city)
            storage.save()
            return jsonify({}), 200
        else:
            abort(404)