#!/usr/bin/env python

'''
SYNOPSIS

    pip install -e .

DESCRIPTION

    Metadata for this package.

REFERENCES

    Building and Distributing Packages with Setuptools
        http://setuptools.readthedocs.io/en/latest/setuptools.html
'''

from setuptools import setup, find_packages


setup(
    name='leginx',
    version='0.1.0',
    description='data processing of goods',
    keywords='http api data goods',
    author='Kevin Leptons',
    author_email='kevin.leptons@gmail.com',
    url='https://github.com/kevin-leptons/leginx',
    download_url='https://github.com/kevin-leptons/leginx',
    python_requires=">=3.4",
    install_requires=[
        'clink==0.20.0', 'click==6.6', 'waitress==1.0.0'
    ],
    packages=find_packages(exclude=['tool', 'test']),
    entry_points={
        'console_scripts': [
            'leginx=leginx.cli:cli',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
    ]
)
