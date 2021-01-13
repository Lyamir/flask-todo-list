from flask import Flask, request, jsonify
from alchemy import SQLAlchemy
from marshmallow import Marshmallow
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)