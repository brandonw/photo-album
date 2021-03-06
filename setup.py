# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import photo_album
version = photo_album.__version__

setup(
    name='photo_album',
    version=version,
    author='',
    author_email='brandon.waskiewicz@gmail.com',
    packages=[
        'photo_album',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['photo_album/manage.py'],
)