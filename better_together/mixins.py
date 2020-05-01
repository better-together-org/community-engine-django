# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class SchedulableMixin(models.Model):
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        abstract = True

    def is_active(self):
        pass


class NameDescriptionMixin(models.Model):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('name'), max_length=255)

    description = models.CharField(_('description'), max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class JoinableMixin(models.Model):

    class Meta:
        abstract = True


class MemberMixin(models.Model):

    class Meta:
        abstract = True


class InvitableMixin(models.Model):

    class Meta:
        abstract = True


class InviteeMixin(models.Model):

    class Meta:
        abstract = True
