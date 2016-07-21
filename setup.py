# coding=utf-8

import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('app/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")
except(IOError, ImportError):
    import io
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="betterlife-psi",
    version=version,
    packages=['app', 'migrations'],
    include_package_data=True,
    author="Lawrence Liu",
    author_email="lawrence@betterlife.io",
    description="Betterlife Intelligent PSI(Purchase, Sales and Inventory) system",
    long_description=long_description,
    license="MIT",
    keywords="Betterlife, Intelligent, Purchase Order, Sales Order, Inventory Management, Retail",
    url="https://github.com/betterlife/psi",
    install_requires=[
        "Flask==0.11.1",
        "sqlalchemy==1.0.14",
        "Flask-SQLAlchemy==2.1",
        "Flask-SSLify==0.1.5",
        "MarkupSafe==0.23",
        "gunicorn==19.3.0",
        "psycopg2==2.6",
        "wsgiref==0.1.2",
        "Flask_BabelEx==0.9.2",
        "Flask-Migrate==1.4.0",
        "raven==5.10.2",
        "Flask-Security==1.7.5",
        "Flask-DebugToolbar==0.10.0",
        "Flask_Admin==1.4.0"
    ],
    dependency_links=[
        "git+https://github.com/betterlife/flask-admin.git@dd26143b3cc1e2bd04a84f86b609306ca25562ee#egg=Flask_Admin-1.4.0"
    ],
    tests_require=[
        "coverage==3.7.1",
        "nose==1.3.7",
        "codecov==2.0.3",
        "fake-factory==0.5.8",
    ],
    setup_requires=['nose==1.3.7'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business :: Financial :: Point-Of-Sale',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Natural Language :: Chinese (Simplified)',
        'Framework :: Flask',
     ],
)