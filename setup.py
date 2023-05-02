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
      version='5.1',
      url='https://github.com/zopefoundation/Products.BTreeFolder2',
      license='ZPL 2.1',
      description="A BTree based implementation for Zope's OFS.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      long_description=(open('README.rst').read()
                        + '\n'
                        + open('CHANGES.rst').read()),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope",
          "Framework :: Zope :: 5",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      python_requires='>=3.7',
      install_requires=[
          'setuptools',
          'AccessControl',
          'Acquisition',
          'BTrees',
          'ExtensionClass>=4.1a1',
          'Persistence',
          'Zope >= 4.0',
          'zope.container',
          'zope.event',
          'zope.lifecycleevent',
      ],
      include_package_data=True,
      zip_safe=False,
      )
