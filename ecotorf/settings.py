"""
Django settings for ecotorf project.

Generated by 'django-admin startproject' using Django 2.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import mimetypes


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+r$_2z^(&od3&lu&ala3(*t!m6t_bmst56*mgw7q1_!%94p!_&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'ekotorf.com', 'www.ekotorf.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'admin_reorder', # django-modeladmin-reorder
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder', # django-modeladmin-reorder
]

ROOT_URLCONF = 'ecotorf.urls'

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

WSGI_APPLICATION = 'ecotorf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'torf',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'u1203339_ekotorf',
            'USER': 'u1203339_default',
            'PASSWORD': '9pbs!Ca4',
            'HOST': 'localhost',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_HOST = 'mail.hosting.reg.ru'
EMAIL_HOST_USER = 'ekotorf.com@ekotorf.com'
EMAIL_HOST_PASSWORD = '9pbs!Ca4'
EMAIL_PORT = 587
#EMAIL_USE_TLS = True
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

ADMIN_REORDER = [
    'ЭкоТорф',
    {'app': 'app', 'label': 'Клиентская Активность', 'models': (
        'app.Applications', 'app.Person', 'app.Feedback',
    )},
    {'app': 'app', 'label': 'Товары', 'models': (
        'app.Product', 'app.ProductGalleryPhoto', 'app.ProductGalleryVideo'
    )},
    {'app': 'app', 'label':  'Почты', 'models': (
        'app.ForMailing', 'app.ForApplications', 'app.ForFeedback', 'app.ForCallback'
    )},
    {'app': 'app', 'label': 'Связь', 'models': (
        'app.TelephoneNumberS', 'app.Viber', 'app.Telegram', 'app.Whatsapp'
    )},
    {'app': 'app', 'label': 'Локация', 'models': (
        'app.WorkingTime', 'app.Geomarker', 'app.MainOffice'
    )},
    {'app': 'app', 'label': 'Контент', 'models': (
        'app.FirstWindow', 'app.StyleMainPage', 'app.PrivacyPolicy', 'app.Faq', 'app.Benefits1',
        'app.Benefits2', 'app.Benefits3', 'app.Benefits4', 'app.Benefits5', 'app.Benefits6',
        'app.Benefits7', 'app.Benefits8',
    )}
]



