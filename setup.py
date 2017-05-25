#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = [
    'ansiwrap>=0.5.4'
]

test_requirements = [
    'ansicolors',
    'tox',
    'pytest',
    'coverage',
    'pytest-cov'
]

setup(
    name='hjoin',
    version='0.1.2',
    description="Horizontal join",
    long_description=readme + '\n\n' + history,
    author="Jonathan Eunice",
    author_email='jonathan.eunice@gmail.com',
    url='https://github.com/jonathaneunice/hjoin',
    packages=[
        'hjoin',
    ],
    package_dir={'hjoin':
                 'hjoin'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='hjoin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='test',
    tests_require=test_requirements
)
