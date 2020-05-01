from django.conf import settings
from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework.routers import APIRootView, DefaultRouter, SimpleRouter

from . import views


class BetterTogetherV1(APIRootView):
    """
    Version 1 of the Better Together API
    """
    pass


class BetterTogetherApis(DefaultRouter):
    APIRootView = BetterTogetherV1

if settings.DEBUG:
    router = BetterTogetherApis(trailing_slash=False)
else:
    router = SimpleRouter()

router.register(r'people', views.PersonViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'memberships', views.MembershipViewSet)
router.register(r'invitations', views.InvitationViewSet)

app_name = 'better_together_api'

api_urlpatterns = [
    path('bt/', RedirectView.as_view(url='api/v1', permanent=False), name='bt_redirect'),
    path('bt/api/', RedirectView.as_view(url='v1', permanent=False), name='bt_api_redirect'),
    path('bt/api/v1/', include(router.urls), name=app_name + '_v1')
]
