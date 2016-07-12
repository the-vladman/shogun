#!/bin/bash
C_FORCE_ROOT=1 celery -A api.v1.resources.tasks worker --detach --loglevel=info --logfile="/root/shogun/shogun.log"
gunicorn api.app:app --workers 3 --timeout 90
