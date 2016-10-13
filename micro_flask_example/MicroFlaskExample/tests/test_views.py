# -*- coding: utf-8 -*-
from flask import url_for


def test_MicroFlaskExample_index(client):
    res = client.get(url_for('MicroFlaskExample_app.index'))
    assert res.data == b'Hello World!'
