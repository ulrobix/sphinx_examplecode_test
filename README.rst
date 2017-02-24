.. -*- restructuredtext -*-

================================
contenttabs extension for Sphinx
================================

:author: Robert Khaliullov <ulrobix@gmail.com>


About
=====

This is a simple extension that, when rendered as HTML, will fold multiple
code blocks containing different programming languages into a single block
which can be toggled from one to another using buttons.

It's intended to be used for displaying example code in multiple languages
(e.g., client code for accessing an API).

This extension adds the ``content-tabs`` directive which adds a class to
a container wrapping the code blocks that should be folded. The class allows
the included Javascript and CSS to render the folded block and buttons.

Quick Example
-------------

Source would look something like this::

    .. content-tabs::

        .. tab-container:: python
            :title: Python

            .. code-block:: python

                import my-api

        .. tab-container:: ruby
            :title: Ruby

            .. code-block:: ruby

                require 'my-api'


This will create an output like this:

.. image:: https://raw.githubusercontent.com/ulrobix/sphinx_examplecode_test/master/_static/example.png
   :alt: Example how it looks like as generated HTML

Example with columns
--------------------

Source would look something like this::

    .. container:: left-col


    .. container:: content-tabs right-col

        .. tab-container:: python
            :title: Python

            .. code-block:: python

                import my-api

        .. tab-container:: ruby
            :title: Ruby

            .. code-block:: ruby

                require 'my-api'

This will create an output like this:

.. image:: https://raw.githubusercontent.com/ulrobix/sphinx_examplecode_test/master/_static/example_cols.png
   :alt: Example how it looks like as generated HTML

Install
=======

From source (tar.gz or checkout)
--------------------------------

Unpack the archive, enter the sphinxcontrib-contenttabs directory and run::

    python setup.py install

Enabling the extension in Sphinx_
---------------------------------

Just add ``sphinxcontrib.contenttabs`` to the list of extensions in the
``conf.py`` file. For example::

    extensions = ['sphinxcontrib.contenttabs']

TODO
====

* Add color configuration options for buttons.

.. Links:
.. _Sphinx: http://sphinx.pocoo.org/`

