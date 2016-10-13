# -*- coding: utf-8 -*-
import json

import pytest

from flask import url_for


def test_swagger_endpoint(client):
    res = client.get(url_for('main_app.swagger'))
    try:
        json.loads(res.data.decode('utf-8'))
    except:
        pytest.fail("Failed to decode swagger specification")