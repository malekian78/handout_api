from .base.py import *

DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']