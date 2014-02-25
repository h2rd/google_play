#!/usr/bin/env python

from setuptools import setup

setup(
    name='google_play',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Google Play app fetcher',
    license="MIT",
    url='https://github.com/h2rd/google_play',
    version='0.1',
    packages=['google_play'],
    test_suite='tests',
    install_requires=(
        'grab==0.4.13',
        'lxml==3.3.1',
        'requests==2.2.1'
    )
)
