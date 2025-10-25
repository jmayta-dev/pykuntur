"""Django production settings for pykuntur project"""

from .base import *


DEBUG = False

MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
