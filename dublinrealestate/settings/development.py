import os
from .settings import *
from decouple import config

if os.path.exists("env.py"):
    import env


DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY_DEVELOPMENT")
ALLOWED_HOSTS = [os.environ.get("DEVELOPMENT_HOST")]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
