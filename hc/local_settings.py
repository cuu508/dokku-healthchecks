""" Read local settings from environment variables. """

import os


DEBUG = os.getenv('HC_DEBUG', False)
# If HC_SECRET_KEY is absent then use a temporary random one
SECRET_KEY = os.getenv("HC_SECRET_KEY", os.urandom(20).encode("hex"))

# HTTP stuff
ALLOWED_HOSTS = os.getenv('HC_ALLOWED_HOSTS', '*').split(",")
SESSION_COOKIE_SECURE = "HC_SESSION_COOKIE_SECURE" in os.environ
CSRF_COOKIE_SECURE = "HC_CSRF_COOKIE_SECURE" in os.environ
SITE_ROOT = os.getenv('HC_SITE_ROOT', "http://localhost:5000")
PING_ENDPOINT = os.getenv('HC_PING_ENDPOINT', SITE_ROOT + "/ping/")
PING_EMAIL_DOMAIN = os.getenv("HC_PING_ENMAIL_DOMAIN", "localhost")

# Generate .gz files in CACHE directory.
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

# Email
DEFAULT_FROM_EMAIL = os.getenv('HC_EMAIL_FROM', "healthchecks@example.org")
EMAIL_HOST = os.getenv('HC_EMAIL_HOST', "localhost")
EMAIL_PORT = int(os.getenv('HC_EMAIL_PORT', 25))
EMAIL_HOST_USER = os.getenv('HC_EMAIL_USER', "")
EMAIL_HOST_PASSWORD = os.getenv('HC_EMAIL_PASSWORD', "")
EMAIL_USE_TLS = EMAIL_PORT == 587

# Database
if os.environ.get("HC_DB") == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("HC_DB_NAME", "hc"),
            'USER': os.getenv('HC_DB_USER', "postgres"),
            'PASSWORD': os.getenv('HC_DB_PASSWORD', ""),
            'HOST': os.getenv('HC_DB_HOST', "localhost"),
            'PORT': os.getenv('HC_DB_PORT'),
            'TEST': {'CHARSET': 'UTF8'}
        }
    }

if os.environ.get("HC_DB") == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': os.getenv('HC_DB_USER', "root"),
            'PASSWORD': os.getenv('HC_DB_PASSWORD', ""),
            'NAME': os.getenv("HC_DB_NAME", "hc"),
            'HOST': os.getenv('HC_DB_HOST', "localhost"),
            'TEST': {'CHARSET': 'UTF8'}
        }
    }

# Sentry
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'raven.contrib.django.raven_compat',  # <-- just adding this

    'hc.accounts',
    'hc.api',
    'hc.front',
    'hc.payments'
)
RAVEN_CONFIG = {"dsn": os.getenv("HC_SENTRY_DSN")}

# Slack
SLACK_CLIENT_ID = os.getenv("HC_SLACK_CLIENT_ID")
SLACK_CLIENT_SECRET = os.getenv("HC_SLACK_CLIENT_SECRET")

# Pushover
PUSHOVER_API_TOKEN = os.getenv("HC_PUSHOVER_API_TOKEN")
PUSHOVER_SUBSCRIPTION_URL = os.getenv("HC_PUSHOVER_SUBSCRIPTION_URL")

# Pushbullet
PUSHBULLET_CLIENT_ID = os.getenv("HC_PUSHBULLET_CLIENT_ID")
PUSHBULLET_CLIENT_SECRET = os.getenv("HC_PUSHBULLET_CLIENT_SECRET")

# Discord
DISCORD_CLIENT_ID = os.getenv("HC_DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = os.getenv("HC_DISCORD_CLIENT_SECRET")

# Braintree
USE_PAYMENTS = "HC_USE_PAYMENTS" in os.environ
if USE_PAYMENTS:
    import braintree
    braintree.Configuration.configure(**{
        "environment": braintree.Environment.Production,
        "merchant_id": os.getenv("HC_BRAINTREE_MERCHANT_ID"),
        "public_key": os.getenv("HC_BRAINTREE_PUBLIC_KEY"),
        "private_key": os.getenv("HC_BRAINTREE_PRIVATE_KEY")
    })
