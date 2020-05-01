=====
Usage
=====

To use better_together in a project, add it to your `INSTALLED_APPS`:

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
