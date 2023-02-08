import os

from django.conf.global_settings import DATETIME_INPUT_FORMATS

DEBUG = (os.getenv('DEBUG') or False)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'apps.root',
]

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

SECRET_KEY = 'foo'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # Enables the server to serve static files in prod

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
