from .base import *

DEBUG = config("DEBUG", cast=bool, default=True)

# Add test-specific settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}