from setuptools import setup

setup(name='SLholidays',
      packages=['SLholidays'],
      version='0.1',
      license='MIT',
      description='A simple library for dealing with holidays.',
      url='https://github.com/rajithst/SLholidays',
      author='Rajith Thennakoon',
      author_email='rajithsthennakoon@gmail.com',
      
      
      zip_safe=False,
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True
      )