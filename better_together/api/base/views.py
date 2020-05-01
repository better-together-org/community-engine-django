from . import serializers
from better_together import models

from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class PersonViewSet(ModelViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    queryset = models.Person.objects.all().order_by('-created_at')
    lookup_field = "slug"
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows Groups to be viewed or edited.
    """
    queryset = models.Group.objects.all().order_by('-created_at')
    lookup_field = "slug"
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(ModelViewSet):
    """
    API endpoint that allows Roles to be viewed or edited.
    """
    queryset = models.Role.objects.all().order_by('-created_at')
    serializer_class = serializers.RoleSerializer
    permission_classes = [permissions.IsAuthenticated]


class MembershipViewSet(ModelViewSet):
    """
    API endpoint that allows Memberships to be viewed or edited.
    """
    queryset = models.Membership.objects.all().order_by('-created_at')
    serializer_class = serializers.MembershipSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvitationViewSet(ModelViewSet):
    """
    API endpoint that allows Invitations to be viewed or edited.
    """
    queryset = models.Invitation.objects.all().order_by('-created_at')
    serializer_class = serializers.InvitationSerializer
    permission_classes = [permissions.IsAuthenticated]