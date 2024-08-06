#!/usr/bin/python3
"""
views
"""

from models import storage
from api.v1.views import app_views

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
