from setuptools import setup

setup(name='SLholidays',
      version='0.1',
      description='A simple library for dealing with holidays.',
      url='https://github.com/rajithst/SLholidays',
      author='Rajith Thennakoon',
      author_email='rajithsthennakoon@gmail.com',
      license='MIT',
      packages=['SLholidays'],
      zip_safe=False,
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True
      )