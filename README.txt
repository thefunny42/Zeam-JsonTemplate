zeam.jsontemplate
*****************

Introduction
============

This library packages a patched version of json template for
`fanstatic`_. This behaved exactly like the official version, except
the option ``undefined_str`` can be a function, that return the value
to use in case of an undefined variable.

.. _`fanstatic`: http://fanstatic.org

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``zeam.jsontemplate``) are published to some URL.

