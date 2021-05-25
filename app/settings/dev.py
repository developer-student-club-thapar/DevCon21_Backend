import os

import environ

from app.settings.base import *

env = environ.Env(DEBUG=(bool, False))
# reading .env file
environ.Env.read_env(env_file=os.path.join(BASE_DIR, "./.env"))  # noqa


# False if not in env
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = []


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # noqa

EMAIL_USE_TLS = True
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

print(EMAIL_HOST_USER)
print(EMAIL_HOST_PASSWORD)
