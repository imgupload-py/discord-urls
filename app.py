#!/usr/bin/env python3
"""
app.py

The main Flask webapp
"""


from flask import Flask, jsonify
from flask_api import status

import encoding


app = Flask(__name__)


@app.route("/encode/<filename>", methods = ["GET"])
def encode(filename):
    return encoding.encode(filename)


@app.route("/decode/<filename>", methods = ["GET"])
def decode(filename):
    try:
        return encoding.decode(filename)
    except encoding.EncodeDecodeError:
        return jsonify({'status': 'error', 'error': 'INCORRECTLY_ENCODED'}), status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    print("Run with `flask` or a WSGI server!")
