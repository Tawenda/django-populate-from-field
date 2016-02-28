#!/usr/bin/env python
#  encoding: utf-8

from distutils.core import setup

setup(name='django-populate-from-field',
      version='1.0',
      description='Field that auto populate from another field or any callable',
      author='Jean-Hugues Pinson',
      author_email='jh.pinson@gmail.com',
      url='',
      packages=['populate_from_field'],
      install_requires=[
          'django'
      ]
      )
