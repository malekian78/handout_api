from decouple import config

ENVIRONMENT = config('DJANGO_ENV', default='production')

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'test':
    from .test import *
else:
    from .local import *