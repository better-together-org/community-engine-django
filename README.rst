=============================
The Better Together Community Engine for Django
=============================

.. image:: https://badge.fury.io/py/better-together-community-engine.svg
    :target: https://badge.fury.io/py/better-together-community-engine

.. image:: https://travis-ci.com/github/better-together-solutions/community-engine-django.svg?branch=master
    :target: https://travis-ci.com/github/better-together-solutions/community-engine-django

.. image:: https://codecov.io/gh/better-together-solutions/community-engine-django/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/better-together-solutions/community-engine-django

The Better Together Community Engine allows devlelopers to quickly model group dynamics in their applications.

Documentation
-------------

The full documentation is at https://better-together-community-engine.readthedocs.io.

Quickstart
----------

Install better_together_community_engine::

    pip install better-together-community-engine

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'better_together_community_engine.apps.BetterTogetherCommunityEngineConfig',
        ...
    )

Add better_together_community_engine's URL patterns:

.. code-block:: python

    from better_together_community_engine import urls as better_together_community_engine_urls


    urlpatterns = [
        ...
        url(r'^', include(better_together_community_engine_urls)),
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
