from setuptools import setup

setup(name='looker-python-sdk',
      version='0.2',
      description='Python SDK for pulling data from Looker',
      url='https://github.com/transverse/looker-python-sdk',
      author='Transverse, LLC',
      author_email='info@gotransverse.com',
      license='MIT',
      packages=['looker'],
      install_requires=['requests'],
      zip_safe=False)