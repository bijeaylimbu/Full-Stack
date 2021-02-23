"""
Django settings for account project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path


import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l5(+-g%nua_^lo*gou%(_9*abqo1%fs%$!(tx5!apizmj5icwu'
# SECRET_KEY=os.environ('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://djangowithreactjs.herokuapp.com']

db_from_env = dj_database_url.config()

# Application definition
django_heroku.settings(locals())
INSTALLED_APPS = [
    'django.contrib.admin',
     'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'corsheaders',
    "rest_framework.authtoken",
    'post_add',
    'account',
    'versatileimagefield',
    "verify_email",
        # 'hitcount',
# 'allauth',
    'auths',
    'django_filters',
    'django_rest_passwordreset',

    "rest_framework_swagger",
'swagger_ui',



# 'rest_email_auth',


]

REST_EMAIL_AUTH = {
'EMAIL_VERIFICATION_URL': 'https://example.com/verify/{key}',
'PASSWORD_RESET_URL': 'https://example.com/reset/{key}',
}


# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#
#     ]
# }


# s


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_ID')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PW')
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'

REST_FRAMEWORK = {
'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
'rest_framework.schemas.coreapi.AutoSchema'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',  # enables simple command line authentication
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
'rest_framework_simplejwt.authentication.JWTAuthentication',

    )
}

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

SITE_ID = 1



#
# JWT_AUTH = {
#     # Authorization:Token xxx
#     'JWT_AUTH_HEADER_PREFIX': 'Token',
# }
# REST_USE_JWT = True


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
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',

]




CORS_ORIGIN_ALLOW_ALL = True
#
# CORS_ALLOW_CREDENTIALS = False

# CORS_ALLOWED_ORIGINS = [
#
#     "http://localhost:3000"
# ]
ROOT_URLCONF = 'account.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'account.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'data',
        'USER':'postgres',
        'PASSWORD':'postgres',
        'HOST':'127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# AUTH_USER_MODEL = 'auths.UserProfile'

MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
#
# AUTHENTICATION_BACKENDS = ('auths.backend.EmailBackend',
#                            "django.contrib.auth.backends.ModelBackend")
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_ID')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PW')
#
# DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'


# SECURE_HSTS_SECONDS = 31536000
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS=True
# SECURE_SSL_REDIRECT=True
# CSRF_COOKIE_SECURE=True
# SECURE_HSTS_PRELOAD=True
# SESSION_COOKIE_SECURE=True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'django_filters',
'cloudinary_storage',
'django.contrib.staticfiles',


]


#
SECURE_HSTS_SECONDS = 31536000
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True


import django_heroku
django_heroku.settings(locals())

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'bijaylimbu11111@gmail.com'
EMAIL_HOST_PASSWORD = 'bijay1111'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "bijaylimbu11111@gmail.com"


# ADMINS = [('Bijay', EMAIL_HOST_USER)]
# MANAGERS = ADMINS




SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}



USE_X_FORWARDED_HOST=True