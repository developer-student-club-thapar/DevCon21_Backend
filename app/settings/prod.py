import os

import dj_database_url

from app.settings.base import *  # noqa

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "p7g_g$a7^qfn!zxc&h+fbvy*0+@trz7)pkr#54elu!1u#rg@tq"
)
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"
ALLOWED_HOSTS = ["devcon21.herokuapp.com"]
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = os.environ.get("EMAIL_PORT", default=587)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")


STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


# database config
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)  # noqa
