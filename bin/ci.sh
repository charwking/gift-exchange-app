#!/usr/bin/env bash

export DB_USER=gift_app_ci_user
export DB_PASS=gift_app_CI_p4s$
export DB_HOST=127.0.0.1
export DB_PORT=8888
export DB_NAME=gift_app_ci_db

# pytest
export WEBTEST_INTERACTIVE=0 # no interactive prompts when tests fail

pipenv run python -m pytest -s test/
