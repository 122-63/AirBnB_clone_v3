#!/usr/bin/python3
"""etrieve an object into a valid JSON"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State