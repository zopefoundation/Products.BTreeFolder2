Changelog
=========

5.0 (2023-02-01)
----------------

- Drop support for Python 2.7, 3.5, 3.6.


4.4 (2022-12-16)
----------------

- Fix Python 2 incompatibility.

- Fix insidious buildout configuration bug for tests against Zope 4.

- Add support for Python 3.10 and 3.11.


4.3 (2021-04-26)
----------------

- Add support for Python 3.9

- Modernize the ZMI template to match the Zope 4 styles
  (`#10 <https://github.com/zopefoundation/Products.BTreeFolder2/issues/10>`_)

- Add ``Delete All Objects`` button to the manage screen.
  (`#9 <https://github.com/zopefoundation/Products.BTreeFolder2/issues/9>`_)


4.2 (2019-03-08)
----------------

- Specify supported Python versions using ``python_requires`` in setup.py
  (`Zope#481 <https://github.com/zopefoundation/Zope/issues/481>`_)

- Drop support for Python 3.4 since Zope itself does not support it.

- Add support for Python 3.8


4.1 (2018-10-05)
----------------

- More PEP8 compliance.

- Add icon for Bootstrap ZMI.

- Avoid deprecation warnings by using current API.

- Add support for Python 3.7.


4.0.0 (2017-05-23)
------------------

- added tox configuration

- Python 3 compatibility

- Update to require and be compatible with Zope 4.

3.0 (2016-07-18)
----------------

- Update Dependencies (no ZODB, but BTrees)

2.14.0 (2015-06-18)
-------------------

- Require ExtensionClass >= 4.1a1 (Compatible w/ Zope 4).

2.13.5 (2015-06-18)
-------------------

- Added case for clean-up routine where the meta type index contains
  keys that are not in the tree.

2.13.4 (2011-12-12)
-------------------

- Provide security declaration for `BTreeFolder2Base.hasObject` method.

- Add some tests for correct `getattr` behavior.

- Minor `__getattr__` and `_getOb` optimizations.

2.13.3 (2011-03-15)
-------------------

- `keys`, `values` and `items` methods are now exactly the same as
  `objectIds`, `objectValues` and `objectItems`. They did the same before
  already but duplicated the code.

2.13.2 (2011-03-08)
-------------------

- `objectValues` and `objectItems` no longer do a special handling when no
  special `spec` is requested as `objectIds` already does the correct
  handling.

2.13.1 (2010-08-04)
-------------------

- Make sure that methods returning objects return them Acquisition wrapped.

- Be more careful in calling our own keys, values and items methods, as
  sub-classes might have overridden some of them.

2.13.0 (2010-07-11)
-------------------

- Changed the `objectIds`, `objectItems` and `objectValues` methods to use the
  internal OOBTree methods directly if no `spec` argument is passed.

- Change implementation of `keys`, `items` and `values` method to access the
  `self._tree` OOBTree methods directly. This avoids lookups in the meta_types
  structures.

- Implement the full dictionary protocol including `__getitem__`,
  `__delitem__`, `__setitem__`, `__nonzero__`, `__iter__` and `__contains__`.

- Released as separate package.
