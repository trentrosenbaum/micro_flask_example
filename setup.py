# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from micro_flask_example import __version__


setup(
    name="micro_flask_example",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["micro_flask_example", "micro_flask_example.MicroFlaskExample"],
    platforms=["any"]
)
