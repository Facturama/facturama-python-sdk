#!/usr/bin/python
# coding: utf-8
# (c) 2017 Raul Granados <@pollitux>

from setuptools import setup, find_packages

version = '2.0.3'
author = 'Tingsystems'

setup(
    name='facturama',
    version=version,
    author=author,
    author_email='soporte@tingsystems.com',
    url='https://github.com/tingsystems/facturama',
    description='Easy Facturama python wrapper',
    long_description=open('./README.txt', 'r').read(),
    download_url='https://github.com/tingsystems/facturama/master',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    install_requires=[
        'requests',
        'simplejson',
        'nose'
    ],
    license='MIT License',
    keywords='facturama wrapper',
    include_package_data=True,
    zip_safe=True,
)
