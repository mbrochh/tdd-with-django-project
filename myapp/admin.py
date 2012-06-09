"""Admin classes for the ``journal`` app."""
from django.contrib import admin

from myapp.models import Entry


admin.site.register(Entry)
