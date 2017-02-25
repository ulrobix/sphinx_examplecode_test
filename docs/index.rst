
sphinxcontrib-contentui
=======================

.. toctree::
   :maxdepth: 2

About
=====

This is a simple extension that, when rendered as HTML, will fold multiple
code blocks containing different operating systems administration examples into a single block
which can be toggled from one to another using buttons.

It's intended to be used for displaying package manager examples.
(e.g., apt install or dnf install).

This extension adds the ``example-code`` directive which adds a class to
a container wrapping the code blocks that should be folded. The class allows
the included Javascript and CSS to render the folded block and buttons.

Currently supported are: Debian, Ubuntu, Fedora, CentOS, OSX

Quick Example
-------------



Installation
------------

.. code-block:: bash

    $ pip install sphinxcontrib-contentui


Enabling the extension in Sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just add sphinxcontrib.examplecode to the list of extensions in the conf.py file. For example:

.. code-block:: bash

    extensions = ['sphinxcontrib.contentui']