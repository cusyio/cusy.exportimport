.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/cusyio/cusy.exportimport/workflows/ci/badge.svg
    :target: https://github.com/cusyio/cusy.exportimport/actions
    :alt: CI Status

.. image:: https://codecov.io/gh/cusyio/cusy.exportimport/branch/main/graph/badge.svg?token=KL4QL32DJR
    :target: https://codecov.io/gh/cusyio/cusy.exportimport
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/v/cusy.exportimport.svg
    :target: https://pypi.python.org/pypi/cusy.exportimport/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/cusy.exportimport.svg
    :target: https://pypi.python.org/pypi/cusy.exportimport
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/cusy.exportimport.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/cusy.exportimport.svg
    :target: https://pypi.python.org/pypi/cusy.exportimport/
    :alt: License


=================
cusy.exportimport
=================

Extensions and patches for collective.exportimport


Features
--------

- Fix wrong ``@id`` for collections:
  https://github.com/collective/collective.exportimport/issues/30


Installation
------------

Install ``cusy.exportimport`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        cusy.exportimport


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/cusyio/cusy.exportimport/issues
- Source Code: https://github.com/cusyio/cusy.exportimport


Support
-------

If you are having issues, please let us know by adding a new ticket.


License
-------

The project is licensed under the GPLv2.
