#!/usr/bin/env bash

# pytest
export WEBTEST_INTERACTIVE=0 # no interactive prompts when tests fail

pipenv run python -m pytest -s test/
