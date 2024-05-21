"""
Django settings for rebutify project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv

load_dotenv()

STAGE = os.getenv("STAGE", "local")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DJANGO_DEBUG", "True") == "True")

ALLOWED_HOSTS: List[str] = (
    os.getenv("DJANGO_HOSTS", "localhost,127.0.0.1").split(",")
    if STAGE != "local"
    else ["localhost", "127.0.0.1"]
)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "core",
    "rest_framework",
    "rebutify",
]

MIDDLEWARE = [
    # CorsMiddleware should be placed as high as possible
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Domains that can access the API
CORS_ALLOWED_ORIGINS = [
    "https://rebutify.org",
    "http://localhost:3000",
    "http://0.0.0.0:3000",
]

# Normalizing URLs for front-end (https://docs.djangoproject.com/en/4.0/ref/middleware/#django.middleware.common.CommonMiddleware)
APPEND_SLASH = False

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

ROOT_URLCONF = "rebutify.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
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


WSGI_APPLICATION = "rebutify.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    if os.getenv("DEBUG_DB", "True") == "True"
    else {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", ""),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", ""),
        "PORT": "5432",
        "CONN_MAX_AGE": 500,
        "CONN_HEALTH_CHECKS": True,
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SECURE_HSTS_SECONDS = int(os.getenv("DJANGO_SECURE_HSTS_SECONDS", 0))

# No effect if HSTS_SECONDS is 0
SECURE_HSTS_PRELOAD = bool(os.getenv("DJANGO_SECURE_SSL_REDIRECT", False))
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(
    os.getenv("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
)

SECURE_SSL_REDIRECT = bool(os.getenv("DJANGO_SECURE_SSL_REDIRECT", False))

SESSION_COOKIE_SECURE = bool(os.getenv("DJANGO_SESSION_COOKIE_SECURE", False))
CSRF_COOKIE_SECURE = bool(os.getenv("DJANGO_CSRF_COOKIE_SECURE", False))

EMAIL_HOST = os.getenv("EMAIL_HOST", "")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", ""))
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS", True))

EMAIL_FROM = os.getenv("EMAIL_FROM", "")
