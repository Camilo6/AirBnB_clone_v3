#!/usr/bin/python3
""" Methods for app_views that return a JSON """
from models.user import User
from models import storage
from flask import Flask, jsonify, make_response, request, abort
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_all():
    """ Returns list of User(s) """
    users_dict = []
    for i in storage.all('User').values():
        users_dict.append(i.to_dict())
    return jsonify(users_dict)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Returns User object"""
    obj = storage.get(User, user_id)
    if obj:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ DELETEs User object"""
    obj = storage.get(User, user_id)
    if obj:
        obj.delete()
        storage.save()
        return {}
    else:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates User"""
    if not request.get_json:
        abort(400, {'Not a JSON'})
    data = request.get_json
    elif 'email' not in data:
        abort(400, {'Missing email'})
    elif 'password' not in data:
        abort(400, {'Missing password'})
    else:
        new_user = User(**data)
        new_user.save()
        return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ PUTs list of user objects """
    if not request.get_json():
        abort(400, {'Not a JSON'})
    data = storage.get(User, user_id)
    if not data:
        abort(404)
    else:
        updt_data = request.get_json()
        for i, j in updt_data.items():
            setattr(data, i, j)
        storage.save()
        return jsonify(data.to_dict())


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_all():
    """ Returns list of User(s) """
    users_dict = []
    for i in storage.all('User').values():
        users_dict.append(i.to_dict())
    return jsonify(users_dict)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Returns User object"""
    obj = storage.get(User, user_id)
    if obj:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ DELETEs User object"""
    obj = storage.get(User, user_id)
    if obj:
        obj.delete()
        storage.save()
        return {}
    else:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates User"""
    if not request.get_json:
        abort(400, {'Not a JSON'})
    data = request.get_json
    elif 'email' not in data:
        abort(400, {'Missing email'})
    elif 'password' not in data:
        abort(400, {'Missing password'})
    else:
        new_user = User(**data)
        new_user.save()
        return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ PUTs list of user objects """
    if not request.get_json():
        abort(400, {'Not a JSON'})
    data = storage.get(User, user_id)
    if not data:
        abort(404)
    else:
        updt_data = request.get_json()
        for i, j in updt_data.items():
            setattr(data, i, j)
        storage.save()
        return jsonify(data.to_dict())
