import os
from decouple import config

settings_module = config('DJANGO_SETTINGS_MODULE', default="core.settings.test")

if not settings_module:
    raise ValueError("The DJANGO_SETTINGS_MODULE environment variable is not set")