# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the contenttabs Sphinx extension.

This extension adds support for a multiple content block
widget to Sphinx.
'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-contenttabs',
    version='0.1.0',
    url='https://github.com/ulrobix/sphinx_contenttabs',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-contenttabs',
    license='BSD',
    author='Robert Khaliullov',
    author_email='ulrobix@gmail.com',
    description='Sphinx "contenttabs" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
