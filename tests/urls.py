# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from better_together.api.base.router import api_urlpatterns as api_v1

from django.conf.urls import url, include
from django.contrib import admin

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include(api_v1)),
]

