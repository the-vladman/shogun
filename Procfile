web: gunicorn api.app:app --workers 3 --timeout 90
worker: celery -A api.v1.resources.tasks worker --loglevel=info
