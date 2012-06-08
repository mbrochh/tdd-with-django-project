"""Factories for the ``myapp`` app."""
import factory

from myapp.models import Entry
from myproject.tests.factories import UserFactory


class EntryFactory(factory.Factory):
    FACTORY_FOR = Entry

    user = factory.SubFactory(UserFactory)
    message = 'A message'
