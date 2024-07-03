from core.settings.base import *

DEBUG = config("DEBUG", cast=bool, default=True)

# For test we should use sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}