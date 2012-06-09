"""Tests for the views of the ``myapp`` app."""
from django.test import TestCase
from django.core.urlresolvers import reverse

from myapp.tests.factories import EntryFactory


class HomeViewTestCase(TestCase):
    """Tests for the ``HomeView`` generic view class."""
    def get_view_name(self):
        return 'home'

    def test_view(self):
        resp = self.client.get(reverse(self.get_view_name()))
        self.assertEqual(resp.status_code, 200)


class EntryDetailViewTestCase(TestCase):
    """Tests for the ``EntryDetailView`` generic view class."""
    def setUp(self):
        self.entry = EntryFactory()

    def get_view_name(self):
        return 'entry_detail'

    def get_view_kwargs(self):
        return {'pk': self.entry.pk}

    def test_view(self):
        resp = self.client.get(reverse(self.get_view_name(),
            kwargs=self.get_view_kwargs()))
        self.assertEqual(resp.status_code, 200)


class EntryListViewTestCase(TestCase):
    """Tests for the ``EntryListView`` generic view class."""
    def setUp(self):
        self.entry1 = EntryFactory()
        self.entry2 = EntryFactory()

    def get_view_name(self):
        return 'entry_list'

    def test_view(self):
        resp = self.client.get(reverse(self.get_view_name()))
        self.assertEqual(resp.status_code, 200)
