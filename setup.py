##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import find_packages
from setuptools import setup


setup(name='Products.BTreeFolder2',
      version='4.4.dev0',
      url='https://github.com/zopefoundation/Products.BTreeFolder2',
      license='ZPL 2.1',
      description="A BTree based implementation for Zope 2's OFS.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=(open('README.rst').read()
                        + '\n'
                        + open('CHANGES.rst').read()),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope :: 2",
          "Framework :: Zope :: 4",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      install_requires=[
          'setuptools',
          'AccessControl',
          'Acquisition',
          'BTrees',
          'ExtensionClass>=4.1a1',
          'future',  # for `cgi/html.escape()`
          'Persistence',
          'six',
          'Zope2 >= 4.0a5',
          'zope.container',
          'zope.event',
          'zope.lifecycleevent',
      ],
      include_package_data=True,
      zip_safe=False,
      )
