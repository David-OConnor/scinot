SciNot
======

This package expresses numbers in scientific notation, in formatted
strings. Its intended use is to make computational results easier to read,
especially when using a REPL like IPython.

Installation:

.. code-block:: bash

    pip install scinot

Python 2 is unsupported, due to unicode handling.

Use: Run scinot.start() to format REPL output and printing as scientific notation.
----------------------------------------------------------------------------------

.. code-block:: python

    341283875012.238
    
>> 341283875012.238

.. code-block:: python

    import scinot

    scinot.start()
    341283875012.238

>> 3.413 x 10 :sup:`11`  

Call scinot.end() to return to remove parsing:

.. code-block:: python

    scinot.end()

    341283875012.238

>> 341283875012.238

You can specify the number of significant figures to display with start, 
and how long the number must be to invoke scientific notation. It defaults
to 4 significant figures, and order-of-magnitude 4:

.. code-block:: python

    scinot.start(sigfigs=2, thresh=3)
    15

>> 15

.. code-block:: python

    152

>> 1.5 x 10 :sup:`2`  


Call scinot.format() to return a string in scientific notation:

.. code-block:: python

    scinot.format(341283875012.238)

>> '3.413 x 10 :sup:`11`'

You can also specify the number of significant figures to display; it
defaults to 3.

.. code-block:: python

    scinot.format(-.00000409348, 2)
    
>> '-4.1 x 10 :sup:`-6`'


Call scinot.disp() instead of scinot.format() to print the result
directly, rather than returning a string. format and disp both take two
arguments: The number, and optionally, the amount of significant figures.

If you're running Python in a Windows terminal and see squares instead of
exponents, try a different font, like Source Code Pro. Scinot's start() behavior
will not work if sympy.init_printing() is activated.

I've built this module with my own use-case in mind, and have likely overlooked
features that would extend and improve functionality. If you have an idea,
please contact me, or submit a pull request.