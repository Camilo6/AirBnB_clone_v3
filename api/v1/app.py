#!/usr/bin/python3
"""
API file
"""

from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler error 404"""
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', 5000),
            debug=True)
