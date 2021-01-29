#!/usr/bin/python3
""" Methods for app_views that return a JSON """
from models.user import User
from models.city import City
from models.place import Place
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, make_response, request, abort


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def list_all(city_id):
    """ Returns list of User(s) """
    city_check = storage.get(City, city_id)
    places_dict = []
    if not city_check:
        abort(404)
    for i in city_check.places:
        places_dict.append(i.to_dict())
    return jsonify(places_dict)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """ Returns User object"""
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """ DELETEs User object"""
    obj = storage.get(Place, place_id)
    if obj:
        obj.delete()
        storage.save()
        return {}
    else:
        abort(404)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    ''' create Place instance '''
    place = storage.get(City, city_id)
    if not place:
        abort(404)
    if not request.json:
        return 'Not a JSON', 400
    data = request.json
    if 'user_id' not in data:
        return 'Missing user_id', 400
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    if 'name' not in data:
        return 'Missing name', 400
    data['city_id'] = city_id
    new_place = Place(**data)
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_Place(place_id):
    """ PUTs list of user objects """
    if not request.json:
        return 'Not a JSON', 400
    data = request.json
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    for i, j in data.items():
        if i not in ['id', 'place_id', 'created_at', 'updated_at']:
            setattr(place, i, j)
    storage.save()
    return jsonify(place.to_dict()), 200
