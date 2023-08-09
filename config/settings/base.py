
from pathlib import Path
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Take environment variables from .env file
env_path = BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(env_path, '.env'))
BASE_DIR = Path(__file__).resolve().parent.parent
# Adding django secret key
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = True

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# con SENTRY

SECRET_KEY = 'FIXME DJANGO SECRET KEY'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'drf_spectacular',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'users',
]

MIDDLEWARE = [
    'config.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('SQL_DBNAME'),
        'USER': env('SQL_USERNAME'),
        "PASSWORD": env('SQL_PASSWORD'),
        "HOST": env('SQL_HOSTNAME'),
        "PORT": env('SQL_PORT')


    }
}

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

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STORAGES = {
    "default": {
        "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
    },
    "staticfiles": {
        "BACKEND": 'storages.backends.s3boto3.S3StaticStorage',
    },
}

AWS_STORAGE_BUCKET_NAME = "FIXME BUCKET NAME"
AWS_S3_ACCESS_KEY_ID = "FIXME ACCESS KEY"
AWS_S3_SECRET_ACCESS_KEY = "FIXME SECRET KEY"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_AUTH = False

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'config.pagination.CustomPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ],
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Panda Django 4.0 REST SERVER API',
    'DESCRIPTION': '🔒authorization -> put token key on header -> {Authorization: Token {key}}',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': '/api',
    "PARSER_WHITELIST": ["rest_framework.parsers.JSONParser"],
    "CAMELIZE_NAMES": True,
    'POSTPROCESSING_HOOKS': [
        'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields'
    ],
}

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "users.serializers.CreateUserSerializer"
}
