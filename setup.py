from setuptools import setup

setup(name='SLholidays',
      packages=['SLholidays'],
      version='0.1',
      license='MIT',
      description='SimpLe Holiday management library for Python,',
      author='Rajith Thennakoon',
      author_email='rajithsthennakoon@gmail.com',
      url='https://github.com/rajithst/SLholidays',
      keywords = ['data analytics','python','holiday','date'],
      install_requires=[],
      classifiers=[
            'Development Status :: 4 - Beta',      
            'Intended Audience :: Developers',      
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',   # Again, pick a license
            'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            ],  
      
      
      zip_safe=False,
      
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True
      )