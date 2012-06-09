#!/bin/bash
# Watches the file system for changes of ``*.py`` files and executes the tests
# whenever you save a file.
watchmedo shell-command --recursive --ignore-directories --patterns="*.py" --wait --command='fab test:integration=0' .
