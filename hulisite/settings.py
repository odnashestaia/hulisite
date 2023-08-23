import os
from pathlib import Path
from dotenv import load_dotenv

# Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]
# End Debug Toolbar

# ENV

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

# end ENV

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

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
    # my app
    # 'day.apps.DayConfig',
    'finances.apps.FinancesConfig',
    'todo.apps.TodoConfig',

    # загруженные библиотеки
    # https://www.django-rest-framework.org/tutorial/quickstart/
    'rest_framework',

    # 'channels'
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # https://django-bootstrap-v5.readthedocs.io/en/latest/installation.html
    'bootstrap5',

    # https://pypi.org/project/django-ckeditor/#required
    # text editor
    'ckeditor',

    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install-the-app
    "debug_toolbar",

    # https://django-crispy-forms.readthedocs.io/en/latest/install.html
    # should be in the end
    'crispy_forms',
    # https://pypi.org/project/crispy-bootstrap4/
    "crispy_bootstrap4",

    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',

    # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Debug Toolbar
]

ROOT_URLCONF = 'hulisite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'hulisite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PW'),
        'HOST': os.getenv('DB_HOST'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'other_static')
]

# end static


# media
# https://docs.djangoproject.com/en/4.1/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'
# end media


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CRISPY_TEMPLATE_PACK = 'uni_form'
# turn on bootstrap4
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# end django-crispy-forms