"""Tests for the models of the ``myapp`` app."""
from django.test import TestCase

from myapp.tests.factories import EntryFactory


class EntryTestCase(TestCase):
    """Tests for the ``Entry`` model class."""
    def test_model(self):
        entry = EntryFactory()
        self.assertTrue(entry.pk)
