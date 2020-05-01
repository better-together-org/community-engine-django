# -*- coding: utf-8 -*-
from django.conf.urls import url, include, re_path
from rest_framework import routers

from . import views


app_name = 'better_together'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'people', views.PersonViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'memberships', views.MembershipViewSet)
router.register(r'invitations', views.InvitationViewSet)

urlpatterns = [
    url(r'^api/v1/bt/', include(router.urls))
]