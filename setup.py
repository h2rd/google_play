#!/usr/bin/env python
from setuptools import setup
from google_play import __version__

setup(
    name='google_play',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Google Play app fetcher',
    license="BSD",
    keywords=['googleplay', 'spider', 'appinfo', 'apps',
              'appsinfo', 'crawler'],
    url='https://github.com/h2rd/google_play',
    version=__version__,
    packages=['google_play'],
    install_requires=[
        'grab==0.4.13',
        'lxml==3.3.1',
        'requests==2.2.1'
    ]
)
