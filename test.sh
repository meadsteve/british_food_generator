#!/usr/bin/env bash
set -ex

pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs british_food_generator/
pipenv run pytest british_food_generator -vv
pipenv run black --check british_food_generator
