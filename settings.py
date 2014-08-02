# -*- coding: utf-8 -*-
#
# va contenir les informations de connexion à la base de données
# le salt qui permet de sécuriser les clefs de hashage
# Django settings for tuto_sdz project

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Cyril Mizzi', 'cyril.mizzi@gmail.com'),
    (u'Natim','natim@siteduzero.com'),
    (u'Cam','cam@siteduzero.com')
)

MANAGERS = ADMINS

DATABASES = {
  'default':{
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'tuto_sdz.db',
    'USERS':'',
    'PASSWORD': '',
    'HOST': '',
    'PORT':'',
  }

}

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

USE_I18N = True

# chemin absolu vers les fichiers statiques CSS, IMG ..
MEDIA_ROOT = '/home/natim/projets-django/tuto_sdz/medias/'

# URL that handles the media served from MEDIA_ROOT
# make sure to use a trailing slash if there is a path component
# examples: 'http://media.lawrence.com', 'http://example.com/media/'
MEDIA_URL = '/medias/'

ADMIN_MEDIA_PREFIX = '/admin-media/'

SECRET_KEY = '7u@2+3jnck=l&a(fwfixa%d+1i8vwf5s14cyj5vyp8hnv5ve=5'

# list of callables that know how to import templates from various sources
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  # 'django.template.loaders.eggs.Loader',
  )

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthentificationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  )

ROOT_URLCONF = 'tuto_sdz.urls'

TEMPLATE_DIRS = (
  '/home/natim/projets-django/tuto-sdz/templates'
  )

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
)

