"""
Django settings for moobo_project project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
# /usr/bin/python
# -*- coding: utf-8 -*-
import os
# import dj_database_url
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'designer')
BASE_DIR_DB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPALTE_DIR = os.path.join(BASE_DIR, 'templates')
STATICFILE_DIR = os.path.join(BASE_DIR, 'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bly!mq_o(-lidt+j4g!e=x7szy@3q8s_p5@9jt@2z_6p*8xn#r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['188.93.210.197', '0.0.0.0', '127.0.0.1', 'moobo.space', 'www.moobo.space', 'doll-cons.ru',
#                  '2018.ip138.com', 'www.baidu.com', 'www.douban.com', 'm.weibo.cn', 'news.sogou.com',
#                  'search.sina.com.cn', 'weixin.sogou.com', 'search.tianya.cn', 'www.toutiao.com',
#                  'news.chinaso.com', '2018.ip138.com', 'fjrb.fjsen.com', 'news.66163.com',
#                  '188-93-210-197.ovz.vps.regruhosting.ru']

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'designer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'moobo_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPALTE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.request",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = 'moobo_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
	    # 'ENGINE': 'django.db.backends.mysql',
	    # 'NAME': 'u1068918_default',
	    # 'USER': 'u1068918_default',
	    # 'PASSWORD': 'B!4ea6Wj',
	    # 'HOST': 'localhost',
	    'ENGINE': 'django.db.backends.sqlite3',
	    'NAME': os.path.join(BASE_DIR_DB, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# import dj_database_url
# db_form_env = dj_database_url.config()
# DATABASES['default'].update(db_form_env)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    STATICFILE_DIR,
]

LOGIN_REDIRECT_URL = '/'

#
# import sys
# sys.setdefaultencoding('utf-8')
#
# import os
# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')


# SECURE_SSL_REDIRECT = False

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'