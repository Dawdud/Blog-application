"""
Django settings for Blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=xyp$w1jb@8$0!%l7l&v@w8c6nfm5jty1m!n15brgv+h7xh+!x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_URL='/pavelstanlley/login/'
#EMAIL SETTINGS
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER='dawdud12@gmail.com'
EMAIL_HOST_PASSWORD= 'Matura8.06.2012'
EMAIL_PORT= 587
EMAIL_USE_TLS= True

#APLICTAION PATHS AND DEBUG
TEMPLATE_DEBUG = True
TEMPLATE_PATH= os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS=(TEMPLATE_PATH,)
TEMPLATE_CONTEXT_PROCESSORS=[
        "django.contrib.auth.context_processors.auth",
        "django.template.context_processors.debug",
        "django.template.context_processors.i18n",
        "django.template.context_processors.request",
        "django.template.context_processors.media",
        "django.template.context_processors.static",
        "django.template.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "pavelstanlley.custom_context_processors.projectlist",
        "pavelstanlley.custom_context_processors.random_post"
]
STATIC_PATH= os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_fo')
STATICFILES_DIRS= (STATIC_PATH,)
ALLOWED_HOSTS = []
MEDIA_URL= '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')

#DISQUS SETTINGS


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pavelstanlley',


)


REGISTRATION_OPEN= True
REGISTRATION_AUTO_LOGIN= True
LOGIN_REDIRECT_URL= '/pavelstanlley/'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Blog.urls'


WSGI_APPLICATION = 'Blog.wsgi.application'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
