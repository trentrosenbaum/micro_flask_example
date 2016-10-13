# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify

from micro_flask_example.swagger import spec

__version__ = '0.1.0'
__all__ = ['create_app']


def create_app():
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from micro_flask_example.views import main_app
    app.register_blueprint(main_app)

    from micro_flask_example.MicroFlaskExample.views import MicroFlaskExample_app
    app.register_blueprint(MicroFlaskExample_app)

    return app

