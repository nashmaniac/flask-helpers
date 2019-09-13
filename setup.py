"""
Author: Raju Ahmed Shetu
"""
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='flask-utilities',
    version='0.3',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple flask utilities that will help to work with flask rest plus',
    long_description=README,
    url='https://github.com/nashmaniac/flask-helpers',
    author='Raju Ahmed Shetu',
    author_email='shetu2153@gmail.com',
    install_requires=[
        'Flask-JWT-Extended>=3.23.0',
        'PyJWT>=1.7.1',
        'aniso8601>=8.0.0',
        'attrs>=19.1.0',
        'Click>=7.0',
        'Flask>=1.1.1',
        'flask-restplus>=0.13.0',
        'itsdangerous>=1.1.0',
        'Jinja2>=2.10.1',
        'jsonschema>=3.0.2',
        'MarkupSafe>=1.1.1',
        'pyrsistent>=0.15.4',
        'pytz>=2019.2',
        'six>=1.12.0',
        'validate-email>=1.3',
        'Werkzeug>=0.15.6',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        # 'Framework :: Flask :: 1.1',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
