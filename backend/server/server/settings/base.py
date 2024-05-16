from datetime import timedelta
from os import getenv, path
import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", True)

# ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "debug_toolbar",
    "rest_framework",
    "corsheaders",
    "djoser",
    "social_django",
    "django_extensions",
    "drf_spectacular",
    # local
    "app.user.apps.UserConfig",
    "app.product.apps.ProductConfig",
    "app.management.apps.ManagementConfig",
    "app.purchases.apps.PurchasesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "ipinfo_django.middleware.IPinfoMiddleware",
    # "app.product.middleware.SimpleMiddleware",
    # "app.user.middleware.AnonymousUserTrackingMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "app.purchases.middleware.AccountMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

IPINFO_TOKEN = "7c77d9047c4e08"
IPINFO_FILTER = lambda request: request.scheme == "http"
IPINFO_FILTER = None

INTERNAL_IPS = ["127.0.0.1"]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),
    }
}

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


CART_SESSION_ID = "cart"
RECENT_VIEWED_SESSION_ID = "recent_viewed_items"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "django_static/"
# STATIC_ROOT = BASE_DIR / "static"
STATIC_ROOT = BASE_DIR / "django_static"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build/static/"),
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "user.UserAccount"

# SESSION_COOKIE_AGE = 1209600

AUTH_COOKIE = "access"
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 60 * 5
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 * 24
# AUTH_COOKIE_SECURE = getenv("AUTH_COOKIE_SECURE", "True") == "True"
AUTH_COOKIE_SECURE = False
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = "/"
AUTH_COOKIE_SAMESITE = "None"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.vk.VKOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "app.user.authentication.CustomJWTAuthentication",
    ],
    # "DEFAULT_PERMISSION_CLASSES": [
    # "rest_framework.permissions.IsAuthenticated",
    # "rest_framework.permissions.AllowAny",
    # ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ROTATE_REFRESH_TOKENS": True,
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=AUTH_COOKIE_ACCESS_MAX_AGE),
    # "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    # "ACCESS_TOKEN_LIFETIME": timedelta(seconds=10),
    # "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(seconds=AUTH_COOKIE_REFRESH_MAX_AGE),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "/password-reset/{uid}/{token}",
    # "USERNAME_RESET_CONFIRM_URL": "/username-reset/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    # "SEND_ACTIVATION_EMAIL": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "TOKEN_MODEL": None,
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "http://localhost:3000/users/google",
        "http://localhost:3000/users/vk",
    ],
    "SERIALIZERS": {
        "current_user": "app.user.serializers.CustomUserSerializer",
    },
    # "SOCIAL_AUTH_ALLOWED_REDIREC_URIS": getenv("REDIRECT_URLS").split(","),
}

# Social OAuth2

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv("GOOGLE_AUTH_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv("GOOGLE_AUTH_SECRET_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]

SOCIAL_AUTH_VK_OAUTH2_KEY = "8120512"
SOCIAL_AUTH_VK_OAUTH2_SECRET = "ZL0mWfSytO4VWQUU7CJJ"

# SOCIAL_AUTH_FACEBOOK_KEY = getenv("FACEBOOK_AUTH_KEY")
# SOCIAL_AUTH_FACEBOOK_SECRET = getenv("FACEBOOK_AUTH_SECRET_KEY")
# SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "email, first_name, last_name"}


# CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
SESSION_SAVE_EVERY_REQUEST = True
# CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]
# CORS_ALLOW_HEADERS = [
#     "Content-Type",  # Add this line to allow Content-Type header
#     # Add any other headers you want to allow here
# ]

# Email settings

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = getenv("SMTP_GMAIL")
EMAIL_HOST_PASSWORD = "txsrqoqatufdlrjz"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Djoser Email Template Text

DOMAIN = getenv("DOMAIN")
SITE_NAME = "Laced"


# DEBUG = False
# PREPEND_WWW = True
# USE_X_FORWARDED_HOST = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SPECTACULAR_SETTINGS = {
    "TITLE": "Your Project API",
    "DESCRIPTION": "Your project description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}
