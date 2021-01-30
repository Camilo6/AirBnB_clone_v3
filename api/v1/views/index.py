#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def Status():
    """Status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def Stats():
    """Stats views"""
    return jsonify(
        {
            'amenities': storage.count("Amenity"),
            'cities': storage.count("City"),
            'places': storage.count("Place"),
            'reviews': storage.count("Review"),
            'states': storage.count("State"),
            'users': storage.count("User")
        })