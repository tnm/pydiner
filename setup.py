#!/usr/bin/env python

import os

from setuptools import setup, find_packages

version = '0.1.0'


LONG_DESCRIPTION = '''

This is an interface to the Diner counting and ranking service for Redis.
Diner itself is at https://github.com/tnm/diner

'''


setup(
    name='pydiner',
    version=version,
    description='A Python interface to the Diner service for Redis',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/tnm/pydiner',
    author='Ted Nyman',
    author_email='tnm800@gmail.com',
    keywords='Redis, data, client, interface',
    license='MIT',
    packages=find_packages(),
    py_modules=['pydiner'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
    'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
   ],
)

