"""Tests for the views of the ``myapp`` app."""
from django.test import TestCase
from django.core.urlresolvers import reverse

from myapp.tests.factories import EntryFactory


class HomeViewTestCase(TestCase):
    """Tests for the ``HomeView`` generic view class."""
    def get_view_name(self):
        """
        I would advise to always define this method.

        As your view grows you will add many more tests which will all call
        ``self.client.get(reverse('name_of_your_view'))``. If you ever decide
        to change that name in your ``urls.py`` you would only have to change
        this string at this central position.

        And trust me: You _will_ change your view name after a while ;)

        """
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
        """
        This is similar to ``get_view_name``. If your view depends on a
        parameter like the object's ID, you would have to pass that parameter
        into the ``reverse`` call many many times as you are writing more and
        more tests. Usually you would always call the view with the same
        parameter, so again, it is better to centralize this here.

        And again: It is quite likely that one day you decide to change
        this parameter, for example when you change your URL style from
        ``/entries/5`` to ``/entries/hello-world``
        (using a slug instead of pk).

        """
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
