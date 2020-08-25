from setuptools import setup

setup(name='pysmm',
      version='0.5.1',
      description='Python Sentinel Soil-Moisture Mapping',
      long_description='For detailed documentation go-to http://pysmm.readthedocs.io/en/latest/',
      classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 2.7',
      ],
      url='https://gitlab.inf.unibz.it/Felix.Greifeneder/pysmm',
      author='Felix Greifeneder',
      author_email='felix.greifeneder@eurac.edu',
      license='GPLv3',
      packages=['pysmm'],
      install_requires=['earthengine-api',
                        'google-api-python-client',
                        'cryptography',
                        'matplotlib',
                        'numpy',
                        'pandas',
                        'pytesmo',
                        'scikit-learn',
                        'scipy'],
      python_requires='>=2.6',
      include_package_data=True,
      zip_safe=False)