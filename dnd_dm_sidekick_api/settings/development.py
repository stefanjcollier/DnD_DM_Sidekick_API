from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += [
  'corsheaders'
]

MIDDLEWARE += [
  'corsheaders.middleware.CorsMiddleware',
]

# we whitelist localhost:3000 because that's where frontend will be served
CORS_ORIGIN_WHITELIST = [
  'https://localhost:3000',
  'http://localhost:3000'
]
