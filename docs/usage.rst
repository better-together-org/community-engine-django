=====
Usage
=====

To use better_together in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'better_together.apps.BetterTogetherConfig',
        ...
    )

Add better_together's URL patterns:

.. code-block:: python

    from better_together import urls as better_together_urls


    urlpatterns = [
        ...
        url(r'^', include(better_together_urls)),
        ...
    ]
