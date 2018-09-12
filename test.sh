#!/usr/bin/env bash
set -ex

pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs core/
pipenv run python manage.py test core --settings british_food_generator.ci_settings
pipenv run black --check british_food_generator core
