"""Django production settings for pykuntur project"""

from .base import *


ALLOWED_HOSTS += ["127.0.0.1","localhost","jmayta.pythonanywhere.com",]

DEBUG = False

MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
