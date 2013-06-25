from settings import *

DATABASES['default']['NAME'] = 'roombo_live'
DATABASES['default']['USER'] = 'roombo_live'
DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
DATABASES['default']['OPTIONS'] = {}

# django-secure settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True


INSTALLED_APPS = INSTALLED_APPS + (
    'djangosecure',
)