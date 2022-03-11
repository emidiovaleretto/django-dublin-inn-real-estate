from .settings import *
from decouple import config

DEBUG = config("DEBUG")
SECRET_KEY = config("SECRET_KEY_DEVELOPMENT")
ALLOWED_HOSTS = [config("HOST")]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
