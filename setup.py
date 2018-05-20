#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python ctrl.compose
"""

from setuptools import setup


install_requires = [
    'ctrl.core',
    'ctrl.config',
    'ctrl.command',
    'docker-compose',
    'pyyaml']
extras_require = {}
extras_require['test'] = [
    "pytest",
    "pytest-mock",
    "coverage",
    "pytest-coverage",
    "codecov",
    "flake8"],

setup(
    name='ctrl.compose',
    version='0.0.1',
    description='ctrl.compose',
    long_description="ctrl.compose",
    url='https://github.com/phlax/ctrl.compose',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python ctrl',
    install_requires=install_requires,
    extras_require=extras_require,
    packages=['ctrl.compose'],
    include_package_data=True)
