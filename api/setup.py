from setuptools import setup

import v2

setup(name='v2',
      version=v2.version,
      description='StackSync API WEB module for OpenStack Swift',
      author='AST Research Group',
      author_email='edgar.zamora@urv.cat, cristian@cotesgonzalez.com, adria.moreno@urv.cat',
      url='',
      packages=['v2'],
      requires=['swift_api(>=1.4)'],
      entry_points={'paste.filter_factory':
                        ['v2=swift2.v2:filter_factory']})
