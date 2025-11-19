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

from setuptools import setup


setup(name='Products.BTreeFolder2',
      version='6.0',
      url='https://github.com/zopefoundation/Products.BTreeFolder2',
      license='ZPL-2.1',
      description="A BTree based implementation for Zope's OFS.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      long_description=(open('README.rst').read()
                        + '\n'
                        + open('CHANGES.rst').read()),
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope",
          "Framework :: Zope :: 5",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Programming Language :: Python :: 3.13",
          "Programming Language :: Python :: 3.14",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      python_requires='>=3.10',
      install_requires=[
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
      )
