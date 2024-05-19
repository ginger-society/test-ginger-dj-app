from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ginger-insecure-u0j2maaxfoo8t1_l(l*asol9gw@(we8j=_lkn9m$dla55^(74@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "ginger.contrib.admin",
    "ginger.contrib.messages",
    "ginger.contrib.staticfiles",
    "ginger.rest_framework",
    "ginger.drf_yasg",
    "ginger.prometheus",
    "src",
]

MIDDLEWARE = [
    "ginger.middleware.security.SecurityMiddleware",
    "ginger.contrib.sessions.middleware.SessionMiddleware",
    "ginger.middleware.common.CommonMiddleware",
    "ginger.middleware.csrf.CsrfViewMiddleware",
    "ginger.contrib.messages.middleware.MessageMiddleware",
    "ginger.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "ginger.template.backends.ginger.GingerTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "ginger.template.context_processors.debug",
                "ginger.template.context_processors.request",
                "ginger.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# Database
# https://docs.ginger.gloportal.dev/en/4.2/ref/settings/#databases

# DATABASES = {  # pragma: no cover
#         "default": {
#             "ENGINE": "ginger.db.backends.postgresql_psycopg2",
#             "NAME": 'test3',
#             "USER": 'postgres',
#             "PASSWORD": 'postgres',
#             "HOST": 'localhost',
#             "PORT": "5432",
#         }
#     }


DATABASES = {
    "default": {
        "ENGINE": "ginger.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

# CACHES = {
#         "default": {
#             "BACKEND": "ginger.core.cache.backends.redis.RedisCache",
#             "LOCATION": "redis://redis:6379",
#         }
#     }

# Internationalization
# https://docs.ginger.gloportal.dev/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.ginger.gloportal.dev/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.ginger.gloportal.dev/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "ginger.db.models.BigAutoField"