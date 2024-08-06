#!/usr/bin/python3
"""
    dou ......c
    """

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status route
    :return: response with json
    """
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
