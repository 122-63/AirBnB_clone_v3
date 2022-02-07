#!/usr/bin/python3
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """method to handle that calls"""
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST")
    if host is None:
        host = "0.0.0.0"
    port = getenv("HBNB_API_PORT")
    if port is None:
        port = "5000"

    app.run(host=host, port=port, threaded=True)
