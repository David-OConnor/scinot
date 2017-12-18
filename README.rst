SciNot
======

This package expresses numbers in scientific notation, in formatted
strings. It's intended use to to make computational results easily readable,
especially when using a REPL like IPython.

Python 2 is unsupported, due to unicode handling.

Example use:

.. code-block:: python

    import scinot

    scinot.parse(341283875012.238)

>> 3.41 x 10 :sup:`11`

You can also specify the number of significant figures to display; it
defaults to 3.

.. code-block:: python

    import scinot

    scinot.parse(-.00000409348, 2)
    
>> -4.1 x 10 :sup:`-6`


You can call scinot.disp(), instead of scinot.parse() to print the result
directly, rather than returning a string. Parse and Disp both take two
arguments: The number, and optionally, the amount of significant figures.

If you're running Python in a Windows terminal and see squares instead of
exponents, try a different font, like Source Code Pro.

I've built this module with my own use-case in mind, and have likely overlooked
features that would extend and improve functionalit. If you have an idea,
please contact me, or submit a pull request.