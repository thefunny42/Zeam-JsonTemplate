zeam.jsontemplate
*****************

Introduction
============

This library packages a patched version of json template for
`fanstatic`_. This behaved exactly like the official version, except
it add an option ``undefined_callable`` that is a function that will
be called in case of an undefined value, to return the value to be
use.

.. _`fanstatic`: http://fanstatic.org

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``zeam.jsontemplate``) are published to some URL.

