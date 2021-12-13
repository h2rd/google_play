#!/usr/bin/env python

from setuptools import setup

setup(
    name='google_play',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Google Play app scrapper',
    license="MIT",
    url='https://github.com/h2rd/google_play',
    version='0.3.0',
    packages=['google_play'],
    test_suite='tests',
    install_requires=(
        'lxml==4.6.5',
        'cssselect==0.9.1',
        'requests[security]',
        'beautifulsoup4==4.3.2'
    )
)
