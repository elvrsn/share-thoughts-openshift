from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='sharethoughts',
      version='1.0',
      description='OpenShift App',
      author='elvrsn',
      author_email='tm.elavarasan@gmail.com',
      url='http://sharethoughts-sharethoughts.rhcloud.com/',
      install_requires=packages,
)

