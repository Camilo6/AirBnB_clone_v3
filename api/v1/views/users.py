#!/usr/bin/python3
"""Methods for app_views that returns a JSON."""
from models.user import User
from models import storage
from flask import Flask, jsonify, make_response, request, abort
from api.v1.views import app_views
