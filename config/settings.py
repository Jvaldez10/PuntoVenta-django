"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path
import config.db as db

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vecinnuu^@uf-t9otczc52$#_5mvk3v2f%lnu$e0_^a%bv54y@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Libs
    "widget_tweaks",
    # Apps
    "core.model1",
    "core.homepage",
    "core.login",
    "core.user",
    "core.reports",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "crum.CurrentRequestUserMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = db.SQLITE


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-pe"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_TMP = os.path.join(BASE_DIR, "static")

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

LOGIN_REDIRECT_URL = "/model1/dashboard/"

LOGOUT_REDIRECT_URL = "/login/"

LOGIN_URL = "/login/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

MEDIA_URL = "/media/"

AUTH_USER_MODEL = "user.User"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# Email

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_HOST_USER = "djangologin99@gmail.com"

EMAIL_HOST_PASSWORD = "0m4gATi3rr@"

DOMAIN = ""
