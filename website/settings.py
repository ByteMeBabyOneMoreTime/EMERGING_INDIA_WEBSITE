"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# django jazzmin config
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Emerging India Foundation",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin Panel",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Emerging India",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": 'logo.png',

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": 'logo_sm.png',

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "welcome to the admin panel",

    # Copyright on the footer
    "copyright": "Emerging India Foundation",
  
    "show_ui_builder": False,
  
    #############
    # Side Menu #
    #############

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    "topmenu_links": [
        {"name": "Home",  "url": "/", "permissions": ["auth.view_user"]},
        {"name": "Gallery Image Upload",  "url": "/gallery/upload", "permissions": ["auth.view_user",  "is_superuser"]},
        {"name": "Gallery News Upload",  "url": "/gallery/upload_news", "permissions": ["auth.view_user",  "is_superuser"]},
        {"name": "Download Data in Excel",  "url": "/forms/download", "permissions": ["auth.view_user",  "is_superuser"]},
        ],

}

# jazzmin UI config
JAZZMIN_UI_TWEAKS = {
    
    "theme": "spacelab",
    
}

# CUSTUM USER MODEL
AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/' 
# Application definition


INSTALLED_APPS = [
    'Home',
    'forms',
    'users',
    'certificates',
    'gallery',
    'pages',
    'payments',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',    # google captcha app
    'django_otp',  #django otp packages
    'django_otp.plugins.otp_totp',  #django otp
    'django_cleanup.apps.CleanupConfig',  #media cleaning app
    'django_admin_search', # admin search module
    'ckeditor',               #cke editor 
    'ckeditor_uploader',         #cke uploader
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',  #django otp middleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', #whitenoise middleware1
    'whitenoise.middleware.WhiteNoiseMiddleware', #whitenoise middleware2
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_TZ = True

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']

# CKE EDITOR SETTINGS
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"

# settings.py

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            # Basic formatting
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['RemoveFormat', 'Format'],
            
            # Headings
            ['Heading1', 'Heading2', 'Heading3', 'Heading4', 'Heading5', 'Heading6'],
            
            # Lists
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            
            # Styles
            ['Blockquote', 'Code'],
            
            # Text alignment
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            
            # Links and images
            ['Link', 'Unlink', 'Image'],
            
            # Media and other elements
            ['EmbedSemantic', 'Table', 'HorizontalRule', 'SpecialChar'],
            
            # Source and others
            ['Source', 'Preview'],
            
            # Show more options
            ['ShowBlocks', 'Maximize'],
        ],
        'removeDialogTabs': 'link:upload;image:upload;image:advanced',
        'extraPlugins': 'image2,autogrow,colorbutton,format,font,justify,widget',
        'image2_disableResizer': True,
        'autoGrow_onStartup': True,
        'autoGrow_maxHeight': 600,
        'autoGrow_bottomSpace': 50,
        'format_tags': 'p;h1;h2;h3;h4;h5;h6',
        'fontSize_sizes': '8/10px;9/11px;10/12px;11/13px;12/14px;14/16px;16/18px;18/20px;20/22px;22/24px;24/26px;26/28px;28/30px',
        'font_names': 'Arial;Comic Sans MS;Courier New;Georgia;Helvetica;Tahoma;Times New Roman;Verdana',
        'colorButton_colors': '000000,FFFFFF,FF0000,00FF00,0000FF,FFFF00,FF00FF,00FFFF',
        'colorButton_textColorNames': 'Black,White,Red,Green,Blue,Yellow,Pink,Cyan',
        'allowedContent': True,  # Allow all HTML elements and attributes
        'extraAllowedContent': 'script; *[*](*); style',  # Allow script tags and inline styles
    }
}

# Razorpay integration
RAZORPAY_API_KEY = 'rzp_live_Hb7aTS9SH5kHYo'
RAZORPAY_API_SECRET = '7tPtm0PwV0Ezj7NuyOcuvCfo'


# google email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 14400


# tinify API Key
TINIFY = os.getenv('TINIFY')

# google recaptcha secret keys
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']



SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID_IMAGES = os.getenv('PARENT_FOLDER_ID_IMAGES')
PARENT_FOLDER_ID_DOCUMENT =os.getenv('PARENT_FOLDER_ID_DOCUMENT')
PARENT_FOLDER_ID_GALLERY = os.getenv('PARENT_FOLDER_ID_GALLERY')

# Enable Gzip compression
WHITENOISE_USE_FINDERS = True

# Enable WhiteNoise's built-in static file compression (for .gzip, .br files)
WHITENOISE_MANIFEST_STRICT = False
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'