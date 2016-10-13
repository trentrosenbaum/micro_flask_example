# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['MicroFlaskExample_app']

MicroFlaskExample_app = Blueprint('MicroFlaskExample_app', __name__)


@MicroFlaskExample_app.route('/')
def index():
    return "Hello World!"
