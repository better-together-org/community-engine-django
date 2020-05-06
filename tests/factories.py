from better_together.models import Person, Group, Role
from typing import Any, Sequence

from factory import DjangoModelFactory, Faker, post_generation, SubFactory

class NameDescriptionFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("job")

    class Meta:
        abstract = True

class PersonFactory(NameDescriptionFactory, DjangoModelFactory):

    class Meta:
        model = Person

class GroupFactory(NameDescriptionFactory, DjangoModelFactory):
    creator = SubFactory(PersonFactory)

    class Meta:
        model = Group

class RoleFactory(NameDescriptionFactory, DjangoModelFactory):

    class Meta:
        model = Role
