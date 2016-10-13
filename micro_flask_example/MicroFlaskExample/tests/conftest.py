# -*- coding: utf-8 -*-
import pytest

from micro_flask_example import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
