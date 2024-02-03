#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery --app=app.tasks.celery_cfg:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery --app=app.tasks.celery_cfg:celery flower
else
  echo "Invalid argument. Please use 'celery' or 'flower'."
fi