#!/usr/bin/env python
from setuptools import setup

setup(
    name='sgp',
    author='Igor Skrynkovskyy',
    author_email='skrynkovskyy@gmail.com',
    description='Simple Google Play interface',
    license="BSD",
    keywords='googleplay spider appinfo leaderboard search developer apps',
    url='https://github.com/h2rd/simple-googleplay',
    version='0.1',
    packages=['sgp'],
    install_requires=[
        'grab==0.4.13',
        'lxml==3.3.1',
        'requests==2.2.1'
    ]
)
