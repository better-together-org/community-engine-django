# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   Person,
   Group,
   Membership,
   Invitation,
   Role,
)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass



