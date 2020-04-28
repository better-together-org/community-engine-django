
from .models import Person, Group, Membership, Invitation, Role
from rest_framework import serializers

class BaseSerializer:
    class Meta:
        fields = ['bt_id', 'created_at', 'updated_at']

class NameDescriptionSerializerMixin:
    class Meta:
        fields = ['name', 'description']

class SchedulableSerializerMixin:
    class Meta:
        fields = ['start', 'end']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + ['url']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + ['url']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + ['url']


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = BaseSerializer.Meta.fields + SchedulableSerializerMixin.Meta.fields + ['url']


class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invitation
        fields = BaseSerializer.Meta.fields + SchedulableSerializerMixin.Meta.fields + ['url']
