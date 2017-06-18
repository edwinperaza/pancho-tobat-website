import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%#$()s9vtud*&6o4am3(q!+e6s2%h+!=zomd_i$y%n4h+e3!t^'
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = (os.getenv('ALLOWED_HOST', '*'),)
SITE_ID = os.getenv('SITE_ID', int(1))
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

ADMINS = (
    (os.getenv('ADMIN_NAME', 'example'),
        os.getenv('ADMIN_EMAIL', 'cris.andrs@gmail.com')),
)

MANAGERS = ADMINS


INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'pancho',
    'home',
    'contacts',
    'services',
    'programs',

    'sorl.thumbnail',
    'django_extensions',
    'django_summernote',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += (
        'debug_toolbar',
    )

ROOT_URLCONF = 'pancho.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'pancho.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pancho',
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'Pancho Tobar',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'contacts': 'icon-book',
    },
    'SEARCH_URL': '',
}

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'es-CL')
TIME_ZONE = os.getenv('TIME_ZONE', 'America/Santiago')
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = os.getenv('STATIC_URL', '/static/')
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')
STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp-relay.sendinblue.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'Wn6E20tbj8kL3MIc')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'bluemix.junio@importadoramoriahdp.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True')


SUMMERNOTE_CONFIG = {
    'width': '100%',
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol', 'height']],
        ['insert', ['link']],
    ],
}
