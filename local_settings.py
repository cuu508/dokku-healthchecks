"""
Local settings for the HealthChecks app
"""

import os


ALLOWED_HOSTS = os.getenv('HC_ALLOWED_HOSTS', '*').split(",")
DEBUG = os.getenv('HC_DEBUG', False)

HOST = os.getenv('HC_HOST', "localhost")
SITE_ROOT = os.getenv('HC_SITE_ROOT', "http://localhost:9090")
PING_ENDPOINT = os.getenv('HC_PING_ENDPOINT', SITE_ROOT + "/ping/")

DEFAULT_FROM_EMAIL = os.getenv('HC_EMAIL_FROM', "healthchecks@example.org")
EMAIL_HOST = os.getenv('HC_EMAIL_HOST', "localhost")
EMAIL_PORT = int(os.getenv('HC_EMAIL_PORT', 25))
EMAIL_HOST_USER = os.getenv('HC_EMAIL_USER', "")
EMAIL_HOST_PASSWORD = os.getenv('HC_EMAIL_PASSWORD', "")
EMAIL_USE_TLS = EMAIL_PORT == 587

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
