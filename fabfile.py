"""Fabfile for the ``myproject`` project."""
from fabric.api import local


def test(integration=1):
    command = './manage.py test -v 2 --settings=myproject.test_settings'
    if int(integration) == 0:
        command += " --exclude='integration_tests'"
    local(command)
