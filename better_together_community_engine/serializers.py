
from .models import Person, Group, Membership, Invitation, Role
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        # fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # fields = ['url', 'name']


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        # fields = ['url', 'name']


class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invitation
        # fields = ['url', 'name']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        # fields = ['url', 'name']
