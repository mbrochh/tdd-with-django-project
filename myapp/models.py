"""Models for the ``myapp`` app."""
from django.db import models


class Entry(models.Model):
    """A comment entry."""
    user = models.ForeignKey('auth.User')
    message = models.TextField()
