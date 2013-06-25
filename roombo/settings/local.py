from .development import *


DATABASES['default']['NAME'] = 'roombo'
DATABASES['default']['USER'] = 'roombo'
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['OPTIONS'] = {
    'autocommit': True,
}
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'