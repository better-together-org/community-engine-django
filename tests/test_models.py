from django.db import IntegrityError
import pytest

from better_together.models import Person, Group, Role, Membership
from django.contrib.contenttypes.fields import GenericRelation
pytestmark = pytest.mark.django_db


def test_person_name(person: Person):
    assert person.name == person.name

def test_group_create_membership(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    assert isinstance(membership, Membership)
    assert group.memberships.count() == 1

def test_group_new_membership_role(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    assert isinstance(membership.role, Role)

def test_group_new_membership_start(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    assert membership.start != None

def test_group_new_membership_end(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    assert membership.end == None

def test_membership_unique_index(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    with pytest.raises(IntegrityError):
        group.create_membership(person, role)

def test_group_is_joinable(group: Group):
    assert group.JoinableMembership == Membership
    assert group.JoinableRole == Role

# def test_group_members_exists(group: Group, person: Person, role: Role):
#     assert group.members.count() == 0
