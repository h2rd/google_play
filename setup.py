#!/usr/bin/env python

from setuptools import setup

setup(
    name='google_play',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Google Play app fetcher',
    license="MIT",
    url='https://github.com/h2rd/google_play',
    version='0.2.0',
    packages=['google_play'],
    test_suite='tests',
    install_requires=(
        'beautifulsoup4==4.3.2',
        'lxml==3.3.1',
        'requests==2.2.1'
    )
)
