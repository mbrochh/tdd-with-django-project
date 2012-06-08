"""Views for the ``myapp`` app."""
from django.views.generic import TemplateView, DetailView

from myapp.models import Entry


class HomeView(TemplateView):
    template_name = 'myapp/home.html'


class EntryDetailView(DetailView):
    model = Entry
