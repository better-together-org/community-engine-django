# -*- coding: utf-8 -*-

import uuid
from django.db import models
from .mixins import NameDescriptionMixin, SchedulableMixin

class BaseModel(models.Model):
    bt_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_people'


class Group(NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_groups'


class Membership(SchedulableMixin, BaseModel):
    class Meta:
        db_table = 'better_together_memberships'
    

class Invitation(SchedulableMixin, BaseModel):
    class Meta:
        db_table = 'better_together_invitations'
    

class Role(NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_roles'
    


