#from setuptools import setup
#setup(name='baas')

from setuptools import setup, find_packages
import sys, os

version = '0.1.1.2'

setup(name='baas',
      version=version,
      description="'Buddy as a Service' is a xmpp / wavelet robot using Yahoo Boss API, Google API and other services to do some stuff for you.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='xmpp',
      author='Martin Borho',
      author_email='martin@borho.net',
      url='http://mborho.github.com/baas',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'twisted',
        'feedparser',
        'chardet',
        'simplejson'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      baas_bot = zeit.care.worker:isofy_main

      """,
      )
