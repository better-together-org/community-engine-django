# -*- coding: utf-8 -*-
# from .joinable.mixins import Joinable, Member
from .mixins import NameDescriptionMixin, SchedulableMixin, SluggedMixin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

JOINABLE_CONTENT_TYPES = []

class BaseModel(models.Model):
    bt_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Joinable(models.Model):

    memberships = GenericRelation(
        'Membership',
        content_type_field='joinable_content_type',
        object_id_field='joinable_id',
        related_name='memberships',
        blank=True,
    )
    # members = models.ManyToManyField(
    #     Member,
    #     related_name='members',
    #     through='memberships',
    #     blank=True
    # )
    # JOINABLE_CONTENT_TYPES += [(self.__class__.__name__, ContentType.objects.get_for_model(self))]

    class Meta:
        abstract = True

    def role_class(self):
        return ContentType.objects.get_for_model(Role)

    def create_membership(self, member, role) -> 'Membership':
        joinable_type = ContentType.objects.get_for_model(self)
        member_type = ContentType.objects.get_for_model(member)

        return Membership.objects.create(
            joinable_content_type=joinable_type,
            joinable_id=self.pk,
            member_content_type=member_type,
            member_id=member.pk,
            role_content_type=self.role_class(),
            role_id=role.pk,
        )



class Member(models.Model):
    # memberships = models.ManyToManyField(
    #     Membership,
    #     related_name='memberships',
    #     blank=True
    # )
    # joinables = models.ManyToManyField(
    #     Joinable,
    #     related_name='joinables',
    #     through='memberships',
    #     blank=True
    # )

    class Meta:
        abstract = True


class Membership(SchedulableMixin, BaseModel):
    joinable_id = models.PositiveIntegerField()
    joinable_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        related_name='joinable_content_type'
    )
    member_id = models.PositiveIntegerField()
    member_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        related_name='member_content_type'
    )
    role_id = models.PositiveIntegerField()
    role_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
        related_name='role_content_type'
    )

    joinable = GenericForeignKey(
        'joinable_content_type',
        'joinable_id'
    )
    member = GenericForeignKey(
        'member_content_type',
        'member_id'
    )
    role = GenericForeignKey(
        'role_content_type',
        'role_id'
    )

    class Meta:
        db_table = 'better_together_memberships'
        unique_together = [
            (
                'joinable_id',
                'joinable_content_type_id',
                'member_id',
                'member_content_type_id',
                'role_id',
                'role_content_type_id',
            ),
        ]



class Person(Member, SluggedMixin, NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_people'

    def slug_source_field(self):
        return 'name'


class Group(Joinable, Member, SluggedMixin, NameDescriptionMixin, BaseModel):
    creator = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
    )

    class Meta:
        db_table = 'better_together_groups'

    def slug_source_field(self):
        return 'name'


class Invitation(SchedulableMixin, BaseModel):
    class Meta:
        db_table = 'better_together_invitations'


class Role(NameDescriptionMixin, BaseModel):
    class Meta:
        db_table = 'better_together_roles'
