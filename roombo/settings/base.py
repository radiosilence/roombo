# coding: utf-8
import os
from unipath import Path
import djcelery
from django.utils.translation import (
    ugettext_lazy as _,
)
import django.conf.global_settings as DEFAULT_SETTINGS

BROKER_URL = 'redis://localhost:6379/0'
djcelery.setup_loader()

APP = 'roombo'
DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = Path(__file__).ancestor(3)

ADMINS = (
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

MANAGERS = ADMINS

AUTH_USER_MODEL = DEFAULT_SETTINGS.AUTH_USER_MODEL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': APP,
        'USER': APP,
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

CACHES = {
    'default' : dict(
        BACKEND='johnny.backends.memcached.MemcachedCache',
        LOCATION=['127.0.0.1:11211'],
        JOHNNY_CACHE=True,
        KEY_PREFIX=APP,
    )
}

THUMBNAIL_QUALITY = 100
THUMBNAIL_COLORSPACE = None
THUMBNAIL_FORMAT = 'PNG'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'
LOCALE_PATHS = (
    PROJECT_ROOT.child('locale'),
)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.child('static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'test')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    'apptemplates.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    #'{app}.context_processors.{app}'.format(app=APP),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'require.storage.OptimizedCachedStaticFilesStorage'

# require.js settings
REQUIRE_BASE_URL = "javascripts"
REQUIRE_BUILD_PROFILE = 'default.build.js'
REQUIRE_JS = "require.js"
REQUIRE_DEBUG = DEBUG
REQUIRE_ENVIRONMENT = 'node'
REQUIRE_STANDALONE_MODULES = {
    "main": {
        # Where to output the built module, relative to REQUIRE_BASE_URL.
        "out": "main-built.js",

        # Optional: A build profile used to build this standalone module.
        "build_profile": "main.build.js",
    }
}

BREADCRUMBS_AUTO_HOME = True
BREADCRUMBS_HOME_TITLE = _('Dashboard')


ROOT_URLCONF = '{app}.urls'.format(app=APP)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{app}.wsgi.application'.format(app=APP)

INSTALLED_APPS = (
    APP,

    'breadcrumbs',
    'djcelery',
    'crispy_forms',
    'require',
    'sorl.thumbnail',
    'south',

    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'