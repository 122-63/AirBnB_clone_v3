#!/usr/bin/python3
"""configuration file"""
from os import getenv
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def teardown(exception):
    """method to handle that calls"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST")
    if host is None:
        host = "0.0.0.0"
    port = getenv("HBNB_API_PORT")
    if port is None:
        port = "5000"

    app.run(host=host, port=port, threaded=True, debug=True)
