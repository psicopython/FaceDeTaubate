from app.config import config
from flask import Flask


def create():
    app = Flask(__name__.strip()[0])
    config(app)
    return app
