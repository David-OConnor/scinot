Scinot
======

This package expresses numbers in scientific notation, in formatted
strings. It's intended use to to make computational results easily readable.

Example use:

.. code-block:: python

    import scinot


    scinot.parse(341283875012.238)
    >> '3.41×10^11'

You can also specify the number of significant figures to display; it
defaults to 3.

.. code-block:: python

    import scinot


    scinot.parse(-.00000409348, 2)
    >> '-4.1×10^-6'