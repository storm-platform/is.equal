..
    Copyright (C) 2021 Storm Project.

    is.equal is free software; you can redistribute it and/or modify
    it under the terms of the MIT License; see LICENSE file for more details.

================
 Is.Equal (?)
================

.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com/storm-platform/is.equal/blob/master/LICENSE
        :alt: Software License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle

.. image:: https://img.shields.io/pypi/dm/is.equal.svg
        :target: https://pypi.python.org/pypi/is.equal

.. image:: https://img.shields.io/github/tag/storm-platform/is.equal.svg
        :target: https://github.com/storm-platform/is.equal/releases

.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord

About
=====

Tool to check if a scientific experiment was reproduced

Usage
-----

.. code-block:: python

    from is_equal import is_equal

    directory_one  = '/path/to/directory/'
    directory_two  = '/path/to/another/dir'

    is_equal(directory_one, directory_two, 'sha256')
