from .base import *

DATABASES['default']['NAME'] = 'roombo_test'
DATABASES['default']['USER'] = 'roombo_test'
DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['default']['OPTIONS'] = {}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'JOHNNY_CACHE': True,
    }
}
EMAIL_BACKEND = 'debugmail.backends.DebugEmailBackend'

HTTP_SECURE = False
SENDFILE_BACKEND = 'sendfile.backends.development'