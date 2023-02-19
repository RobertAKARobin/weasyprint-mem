import os

from debug_toolbar import settings as debug_toolbar_settings

DEBUG = os.getenv('DEBUG') or False

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'pympler',

    'apps.root',
]

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'foo'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'pympler.panels.MemoryPanel',
)

def show_toolbar(request):
    return (request.path == '/')

DEBUG_TOOLBAR_CONFIG = {
    **debug_toolbar_settings.CONFIG_DEFAULTS,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

HOST_URI = None # See lib.urls.CacheHostAddressMiddleware

APPEND_SLASH = True

ROOT_URLCONF = 'apps.root.urls' # A string representing the full Python import path to your root urls.py

INTERNAL_IPS = (
    '127.0.0.1',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'apps/root/templates'),
        ],
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ),
        },
    },
]

# The absolute path to the directory where collectstatic gathers static files. Not used during dev.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# In prod, uses cache-busting
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    # Will find files stored in the STATICFILES_DIRS setting
    'django.contrib.staticfiles.finders.FileSystemFinder',

    # Will find files in the 'static' subdirectory of each app
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled
STATICFILES_DIRS = [
    'static',
]

FILE_CHARSET = 'utf-8'
