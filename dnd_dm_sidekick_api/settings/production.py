import django_heroku
import dj_database_url
from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

INSTALLED_APPS += [
  'corsheaders'
]

MIDDLEWARE += [
  'corsheaders.middleware.CorsMiddleware',
]

# we whitelist localhost:3000 because that's where frontend will be served
CORS_ORIGIN_WHITELIST = [
  'https://dm-sidekick.herokuapp.com',
]

# must be last
django_heroku.settings(locals())
