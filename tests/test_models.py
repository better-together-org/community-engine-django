from django.db import IntegrityError
import pytest

from better_together.models import Person, Group, Role, Membership

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

def test_membership_unique_index(group: Group, person: Person, role: Role):
    membership = group.create_membership(person, role)
    with pytest.raises(IntegrityError):
        group.create_membership(person, role)
