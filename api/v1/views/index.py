#!/usr/bin/python3
"""
index view
"""

from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """status"""
    return jsonify({"status": "OK"})
