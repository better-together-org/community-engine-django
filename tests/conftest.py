import pytest

from better_together.models import Person, Group, Role
from .factories import PersonFactory, GroupFactory, RoleFactory


@pytest.fixture
def person() -> Person:
    return PersonFactory()


@pytest.fixture
def group() -> Group:
    return GroupFactory()


@pytest.fixture
def role() -> Role:
    return RoleFactory()
