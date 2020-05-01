from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r'people', views.PersonViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'roles', views.RoleViewSet)
# router.register(r'memberships', views.MembershipViewSet)
# router.register(r'invitations', views.InvitationViewSet)

app_name = 'api'
api_urlpatterns = [
    path('api/v1/bt/', include(router.urls))
]
