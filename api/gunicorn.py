import os

if os.environ.get('MODE') == 'dev':
    reload = True

bind = '0.0.0.0:80'
errorlog = 'gunicorn_error.log'
loglevel = 'error'
