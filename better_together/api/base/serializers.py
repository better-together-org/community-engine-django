from rest_framework import serializers

from better_together import models


class BaseSerializer:
    class Meta:
        fields = ['bt_id', 'created_at', 'updated_at']

class NameDescriptionSerializerMixin:
    class Meta:
        fields = ['name', 'description']

class SchedulableSerializerMixin:
    class Meta:
        fields = ['start', 'end']

class SluggedSerializerMixin:
    class Meta:
        fields = ['slug']

        extra_kwargs = {
            "url": { "lookup_field": "slug"}
        }

class PersonSerializer(serializers.ModelSerializer):
    class Meta(SluggedSerializerMixin.Meta):
        model = models.Person
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + SluggedSerializerMixin.Meta.fields + ['url']


class GroupSerializer(SluggedSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta(SluggedSerializerMixin.Meta):
        model = models.Group
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + ['url']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = BaseSerializer.Meta.fields + NameDescriptionSerializerMixin.Meta.fields + ['url']


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Membership
        fields = BaseSerializer.Meta.fields + SchedulableSerializerMixin.Meta.fields + ['url']


class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Invitation
        fields = BaseSerializer.Meta.fields + SchedulableSerializerMixin.Meta.fields + ['url']
