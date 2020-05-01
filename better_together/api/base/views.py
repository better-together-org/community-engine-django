from . import serializers
from better_together import models

from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet



class PersonViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    """
    API endpoint that allows People to be viewed or edited.
    """
    queryset = models.Person.objects.all().order_by('-created_at')
    lookup_field = "name"
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated]