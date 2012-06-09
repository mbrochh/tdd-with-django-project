"""Views for the ``myapp`` app."""
from django.views.generic import TemplateView, DetailView, ListView

from myapp.models import Entry


class HomeView(TemplateView):
    template_name = 'myapp/home.html'


class EntryListView(ListView):
    model = Entry


class EntryDetailView(DetailView):
    model = Entry
