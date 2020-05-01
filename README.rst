=============================
The Better Together Community Engine for Django
=============================

.. image:: https://badge.fury.io/py/better-together-community-engine.svg
    :target: https://badge.fury.io/py/better-together-community-engine

.. image:: https://travis-ci.com/better-together-solutions/community-engine-django.svg?branch=master
    :target: https://travis-ci.com/better-together-solutions/community-engine-django

.. image:: https://codecov.io/gh/better-together-solutions/community-engine-django/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/better-together-solutions/community-engine-django

.. image:: https://readthedocs.org/projects/better-together-community-engine-django/badge/?version=latest
    :target: https://better-together-community-engine-django.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

The Better Together Community Engine allows devlelopers to quickly model group dynamics in their applications.

Documentation
-------------

The full documentation is at https://better-together-community-engine-django.readthedocs.io.

Quickstart
----------

Install better_together::

    pip install django-better-together

Add it to your `INSTALLED_APPS`:

.. code-block:: python
    
    import better_together


    BETTER_TOGETHER_APPS = better_together.get_core_apps()
    
    INSTALLED_APPS = (
        ...
        ...
    ) + BETTER_TOGETHER_APPS

Add better_together's URL patterns:

.. code-block:: python

    from better_together.api.base.router import api_urlpatterns as bt_api_v1


    urlpatterns = [
        ...
        path('', include(bt_api_v1)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
