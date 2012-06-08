"""Fabfile for the ``myproject`` project."""
from fabric.api import local


def dumpdata():
    """
    Calls dumpdata for all apps.

    Remember to add new dumpdata commands for new apps here so that you always
    get a full initial dump when running this task.

    """
    local('python2.7 ./manage.py dumpdata --indent 4 --natural auth --exclude auth.permission > myproject/fixtures/bootstrap_auth.json')  # NOQA
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sites > myproject/fixtures/bootstrap_sites.json')  # NOQA


def loaddata():
    """
    Loads the bootstrap fixtures so you can start clicking around on the site.

    """
    local('python2.7 manage.py loaddata bootstrap_auth.json')
    local('python2.7 manage.py loaddata bootstrap_sites.json')
    local('python2.7 manage.py loaddata bootstrap.json')


def rebuild():
    """
    Deletes the database and recreates the database and bootstrap fixtures.

    """
    local('./manage.py reset_db --router=default --noinput')
    local('python2.7 manage.py syncdb --all --noinput')
    local('python2.7 manage.py migrate --fake')
    loaddata()
    local('./manage.py collectstatic --noinput')


def test(integration=1):
    command = './manage.py test -v 2 --settings=myproject.test_settings'
    if int(integration) == 0:
        command += " --exclude='integration_tests'"
    local(command)
