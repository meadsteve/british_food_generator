#!/usr/bin/env bash
gunicorn british_food_generator:app --log-level info -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000