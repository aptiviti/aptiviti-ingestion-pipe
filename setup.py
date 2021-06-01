# _*_ coding: utf-8 _*_
from setuptools import find_packages
from distutils.core import setup

setup(
    name='aptiviti-ingestion-pipe',
    version='1.0.1',
    author='Daniel Fredriksen',
    author_email='df@etr.ai',
    packages=find_packages(),
    url='https://github.com/aptiviti/aptiviti-ingestion-pipe',
    license='AGPLv3',
    description='Aptiviti wrapper for data ingestion provider'
)