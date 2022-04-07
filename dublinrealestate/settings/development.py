from .settings import *
from decouple import config

DEBUG = True
SECRET_KEY = config("SECRET_KEY_DEVELOPMENT")
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
