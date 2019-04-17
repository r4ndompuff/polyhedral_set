from setuptools import setup, find_packages
from os.path import join, dirname
import lin

setup(
    name='lin',
    version=lin.__version__,
    description='a pip-installable package example',
    license='MIT',
    packages=find_packages(),
    author='Andrey Love',
    author_email='r4nd0m1999@gmail.com',
	install_requires=[
    	'NumPy==1.15.4'
	],
    keywords=['linear programming', 'polyhedral set', 'extreme points'],
    url='https://github.com/r4ndompuff/polyhedral_set'
)