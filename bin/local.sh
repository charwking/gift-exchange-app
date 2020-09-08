#!/usr/bin/env bash

export DB_USER=gift_app_local_user
export DB_PASS='gift_app_LOCAL_p4s$'
export DB_HOST=localhost
export DB_PORT=3306
export DB_NAME=gift_app_local_db
export DB_ECHO_SQL=true

export SERVER_PORT=5000

pipenv run python -m src
