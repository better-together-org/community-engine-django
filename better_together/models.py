# -*- coding: utf-8 -*-

import uuid
from django.db import models
from .mixins import NameDescriptionMixin, SchedulableMixin, SluggedMixin

class BaseModel(models.Model):
    bt_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(SluggedMixin, NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_people'

    def slug_source_field(self):
        return 'name'


class Group(SluggedMixin, NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_groups'

    def slug_source_field(self):
        return 'name'


class Membership(SchedulableMixin, BaseModel):
    class Meta:
        db_table = 'better_together_memberships'
    

class Invitation(SchedulableMixin, BaseModel):
    class Meta:
        db_table = 'better_together_invitations'
    

class Role(NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_roles'
    


