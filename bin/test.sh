#!/usr/bin/env bash

export DB_USER=gift_app_test_user
export DB_PASS=gift_app_TEST_p4s$
export DB_HOST=localhost
export DB_PORT=3306
export DB_NAME=gift_app_test_db

# pytest
export WEBTEST_INTERACTIVE=0 # no interactive prompts when tests fail

pipenv run python -m pytest -s test/
