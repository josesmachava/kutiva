"""
Django settings for kutiva project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


USE_I18N = True


LANGUAGE_CODE = 'en'



LANGUAGES = (
    ('pt_BR', _('Portuguese')),
    
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cqd9i9ua1mo@zbr2r41sm3)pd5__a_r1%4h^=tc^+z9p)z(mfg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
                 "*",
                 "kutiva.co.mz",
                 "www.kutiva.co.mz",
                  "kutiva.herokuapp.com",
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django.contrib.humanize',
    'graphene_django',
    'crispy_forms',
    'storages',
    'community',
    'embed_video',
    'api',
    's3direct',
    'tinymce',
    'account',
    'corsheaders',
    'cms',
    'payment',
    'hitcount',
  
    
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

GRAPHENE = {
    'SCHEMA': 'kutiva.schema.schema' # Where your Graphene schema lives
}

AUTH_USER_MODEL = 'account.User'
LOGIN_URL='signin'
LOGOUT_REDIRECT_URL = 'index'


CRISPY_TEMPLATE_PACK = 'bootstrap4'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'kutiva.urls'


EMAIL_HOST = 'mail.kutiva.co.mz'
EMAIL_PORT = 26
EMAIL_HOST_USER = 'noreply@kutiva.co.mz'
EMAIL_HOST_PASSWORD = '849394995Jose'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@kutiva.co.mz'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'kutiva/templates')
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # PyPugJS part:
            'loaders': [
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': [
                'pypugjs.ext.django.templatetags',
            ],
        },
    },
]


WSGI_APPLICATION = 'kutiva.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# Parse database configuration from $DATABASE_URL
# Enable Persistent Connections



try:
    from .settings_local import *
except ImportError:

    ALLOWED_HOSTS = ['*']

    ADMINS = [('Guidione  Machava', 'geral.market.co.mz@gmail.com'),
              ('Jose Machava', 'josesmachava@gmail.com'), ]
    # Parse database configuration from $DATABASE_URL
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
    # Enable Persistent Connections

   


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'Africa/Maputo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'kutiva', 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'kutia/static'),
# ]
#
# AWS_ACCESS_KEY_ID = 'AKIAIVY7VBM57EMJRKIQ'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'museucinema-static'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
#
# AWS_LOCATION = 'static'
# # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#
# DEFAULT_FILE_STORAGE = 'kutiva.storage_backends.MediaStorage'



AWS_ACCESS_KEY_ID = 'AKIA4Y4LY4AEPAH4TGNG'
AWS_SECRET_ACCESS_KEY = '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'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'kutiva'
AWS_S3_REGION_NAME = 'us-east-2'




