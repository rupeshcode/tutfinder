"""
Django settings for tutfinder project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e&9!tyxvdtil^y)rl95=ixo9j5kfl%gv49v5k64+teok2hcqh9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'course',
    'core',
    'review',
    'technology',
    'track',
    'track_course',
    'profile',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'tutfinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tutfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),

]

CORS_ORIGIN_ALLOW_ALL = True
#setting upload paths for ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
#ckeditor uses pillow for image backend
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
    },
}
#saw it some where
CKEDITOR_ALLOW_NONIMAGE_FILES = True


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#     ),
# }

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # )
    "DEFAULT_AUTHENTICATION_CLASSES": (
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'rest_framework.authentication.BasicAuthentication'

    ),
    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('JWT', 'Bearer'),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
'''
curl -X POST -d "username=cfe&password=learncode" http://127.0.0.1:8000/api/auth/token/
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw
" http://127.0.0.1:8000/api/comments/
curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY2MTc4fQ._i5wEqJ_OO8wNiVVNAWNPGjGaO7OzChY0UzONgw06D0" -H "Content-Type: application/json" -d '{"content":"some reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'
curl http://127.0.0.1:8000/api/comments/
curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5MzkyMzUyOWNkNjM0ODlhOWU2MjY4MjM4MmU3MzNlYSIsInRva2VuX3R5cGUiOiJhY2Nlc3MiLCJleHAiOjE1MjkwOTMzMDcsInVzZXJfaWQiOjF9.WIImQM8XKS9klkiEOdFAtO_50vI5tbYNbg3ERFlgp6c" -H "Content-Type: application/json" -d '{"title":"javascript"}' 'http://127.0.0.1:8000/api/technology/create/'
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImp0aSI6IjI3ODk2NTU2MGRkODQ5YmVhNGQzNjE1ZmM1ZTI1NDg3IiwiZXhwIjoxNTI5MTc2Mjc1LCJ1c2VyX2lkIjoxfQ.ueOuBdUxvwQd5tEKw1uxfVaxOGWZqrGMIsEM1uPoGS8"}' \
  http://localhost:5000/api/auth/token/refresh/
curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwidXNlcl9pZCI6MywiZXhwIjoxNTI5OTUyMzA2LCJqdGkiOiJhYWEyOTYyNjE1NTE0Y2NmYTg1NGI3Y2E1NTU0NzE1YSJ9.PaHUhtSgHbLqBTt08oQBd2eMczTjYwRKRjparTDsjHc" -H "Content-Type: application/json" -d '{}' 'http://127.0.0.1:8000/api/users/detail/'
'''