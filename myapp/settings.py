from pathlib import Path
import os
import sys
import dj_database_url
import env

DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.DEBUG
USE_AWS = env.USE_AWS

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", env.AWS_ACCESS_KEY_ID)
# DATABASE_URL = env.DATABASE_URL
# DATABASE_DB = env.DATABASE_DB

DEVELOPMENT_MODE = env.DEVELOPMENT_MODE

ALLOWED_HOSTS = (
    "127.0.0.1",
    "localhost",
    "clubsforfun.com",
    "www.clubsforfun.com",
    "clubswing.co.uk",
    "www.clubswing.co.uk",
)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sorl.thumbnail",
    "gunicorn",
    "django_extensions",
    "django_select2",
    "django.contrib.gis",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "storages",
    "crispy_forms",
    "crispy_bootstrap5",
    "formtools",
    "profanity",
    "request",
    "blog",
    "event",
    "feed",
    "friend",
    "gallery",
    "groups",
    "messaging",
    "notifications",
    "pages",
    "parties",
    "place_area",
    "profiles",
    "search",
    "report",
    # This app must be the last app
    "django_cleanup.apps.CleanupConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "request.middleware.RequestMiddleware",
]


ROOT_URLCONF = "myapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "myapp/templates")],
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
CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = "myapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

SESSION_ENGINE = "django.contrib.sessions.backends.db"

if DEVELOPMENT_MODE == "True":
    if os.name == "nt":
        import platform

        OSGEO4W = r"C:\\OSGeo4W"
        # if '64' in platform.architecture()[0]:
        #     OSGEO4W += "64"
        assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
        os.environ["OSGEO4W_ROOT"] = OSGEO4W
        os.environ["GDAL_DATA"] = OSGEO4W + r"\share\gdal"
        os.environ["PROJ_LIB"] = OSGEO4W + r"\share\proj"
        os.environ["PATH"] = OSGEO4W + r"\bin;" + os.environ["PATH"]
        print("DEVELOPMENT_MODE = True")
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.sqlite3",
    #         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    #     }
    # }

    GDAL_LIBRARY_PATH = "C:\\OSGEO4W\\bin\\gdal309"
    print(os.path.join(BASE_DIR, "db.sqlite3"))
elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
    print("DEVELOPMENT_MODE = False")


DATABASES = {
    "default": {
        "ENGINE": env.DATABASE_ENGINE,
        "NAME": env.DATABASE_NAME,
        "USER": env.DATABASE_USER,
        "PASSWORD": env.DATABASE_PASS,
        "HOST": env.DATABASE_HOST,
        "PORT": env.DATABASE_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
if USE_AWS == "True":
    # aws settings
    STATICFILES_LOCATION = "static"
    MEDIAFILES_LOCATION = "media"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", env.AWS_ACCESS_KEY_ID)
    AWS_STORAGE_BUCKET_NAME = os.getenv(
        "AWS_STORAGE_BUCKET_NAME", env.AWS_STORAGE_BUCKET_NAME
    )
    AWS_SECRET_ACCESS_KEY = os.getenv(
        "AWS_SECRET_ACCESS_KEY", env.AWS_SECRET_ACCESS_KEY
    )

    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # s3 static settings
    AWS_LOCATION = "static"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_STORAGE)
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)

else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Uncomment if you have extra static files and a directory in your GitHub repo.
# If you don't have this directory and have this uncommented your build will fail
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

ACCOUNT_SIGNUP_REDIRECT_URL = "/set_profile_type/"
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT = "/login/"
ACCOUNT_PRESSERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/set_profile_type/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/set_profile_type/"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_USERNAME_BLACKLIST = (
    "page",
    "pages",
    "add_page",
    "claim_page",
    "edit_page",
    "new_page_post",
    "add_review",
    "add_host",
    "page_feed",
    "page_gallery",
    "page_reviews",
    "page_follow",
    "edit_profile",
    "feed",
)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", env.EMAIL_HOST_USER)
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", env.EMAIL_HOST_PASSWORD)
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", env.DEFAULT_FROM_EMAIL)

CSRF_TRUSTED_ORIGINS = [
    "https://clubswing.co.uk",
    "https://www.clubswing.co.uk",
    "https://clubsforfun.com",
    "https://www.clubsforfun.com",
]
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_AGE = 30 * 60  # 60 minutes. "1209600(2 weeks)" by default

SESSION_SAVE_EVERY_REQUEST = False  # "False" by default


REQUEST_TRAFFIC_MODULES = {
    "request.traffic.UniqueVisitor",
    "request.traffic.UniqueVisit",
    "request.traffic.Hit",
}

REQUEST_IGNORE_PATHS = (r"^admin/",)

# REQUEST_BASE_URL = {'https://%s' % Site.objects.get_current().domain}
