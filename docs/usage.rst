=====
Usage
=====

To use better_together_community_engine in a project, add it to your `INSTALLED_APPS`:

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
