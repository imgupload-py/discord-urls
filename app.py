#!/usr/bin/env python3
"""
app.py

The main Flask webapp
"""


from flask import Flask, jsonify, redirect, render_template
from flask_api import status

import encoding
import settings


app = Flask(__name__)


@app.route("/encode/<filename>", methods = ["GET"])
def encode(filename):
    return encoding.encode(filename)


@app.route("/decode/<filename>", methods = ["GET"])
def decode(filename):
    try:
        return encoding.decode(filename)
    except encoding.EncodeDecodeError:
        print("filename doesn't contain only 200b and 200c")
        return jsonify({'status': 'error', 'error': 'INCORRECTLY_ENCODED'}), status.HTTP_400_BAD_REQUEST


@app.route("/v1/fancy/<image>", methods = ["GET"])
def fancy(image):
    try:
        decimg = encoding.decode(image)
    except encoding.EncodeDecodeError:
        print("filename doesn't contain only 200b and 200c")
        return jsonify({'status': 'error', 'error': 'INCORRECTLY_ENCODED'}), status.HTTP_400_BAD_REQUEST
    return redirect(settings.ROOTURL + decimg, 307)


@app.route("/v1/discord/<image>", methods = ["GET"])
def discord(image):
    try:
        decimg = encoding.decode(image)
    except encoding.EncodeDecodeError:
        print("filename doesn't contain only 200b and 200c")
        return jsonify({'status': 'error', 'error': 'INCORRECTLY_ENCODED'}), status.HTTP_400_BAD_REQUEST
    return render_template("discord.html", url = settings.ROOTURL + decimg)


if __name__ == "__main__":
    print("Run with `flask` or a WSGI server!")
