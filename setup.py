#!/usr/bin/env python3

import os
import setuptools

here = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(here, 'README.rst')) as readme:
    long_description = readme.read()

setuptools.setup(
    name='onedrive',
    version='0.0.1dev',
    description='bare bones OneDrive uploader',
    long_description=long_description,
    url='https://github.com/zmwangx/pyonedrive',
    author='Zhiming Wang',
    author_email='zmwangx@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='onedrive upload',
    packages=['onedrive'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'onedrive-upload=onedrive.cli:cli_upload',
            'onedrive-geturl=onedrive.cli:cli_geturl',
        ]
    },
    test_suite='tests',
)