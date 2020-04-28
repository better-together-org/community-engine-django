# -*- coding: utf-8 -*-
from django.conf.urls import url, include, re_path
from rest_framework import routers

from . import views


app_name = 'better_together'

bt_router = routers.DefaultRouter(trailing_slash=False)
bt_router.register(r'people', views.PersonViewSet)
bt_router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^bt/v1/', include(bt_router.urls))
]