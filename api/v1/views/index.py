#!/usr/bin/python3
"""
    dou ......c
    """

from api.v1.views import app_view
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=True)
