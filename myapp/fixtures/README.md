The fixtures in this directory should ALWAYS only be created via the
``fab dumpdata`` command.

The workflow would be as follows:

* You realize that you would like to have more fixtures for bootstrapping the
  project
* You add the objects using the Django admin interface
* You call ``fab dumpdata``
* You use ``git diff`` to make sure that the changes dumpdata created are sane
* You run ``fab rebuild`` to see if your project can still be bootstrapped
  with your new fixture files
* You run ``./manage.py runserver`` and check if the new objects are displayed
  as expected
* If it anything fails, you can run ``git co .`` to revert your dumpdata call,
  fix the issue and try again
* If all is good, you run ``git add . && git commit``
