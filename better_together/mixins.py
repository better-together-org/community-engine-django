# -*- coding: utf-8 -*-
from .utils import unique_slug_generator
from django.db import models
from django.utils.translation import gettext_lazy as _


class SchedulableMixin(models.Model):
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        abstract = True

    def is_active(self):
        pass


class SluggedMixin(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, source_model_field=self.slug_source_field(), output_model_field="slug")

        super().save(*args, **kwargs)

    def slug_source_field(self):
        return 'name'


class NameDescriptionMixin(models.Model):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('name'), max_length=255)

    description = models.CharField(_('description'), max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


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
