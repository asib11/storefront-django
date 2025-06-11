from .common import *
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    MIDDLEWARE += [
        'silk.middleware.SilkyMiddleware',
    ]



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront',
#         'HOST': 'localhost',
#         'USER': 'root',
#         'PASSWORD': 'your_new_password',
#     }
# }
DATABASES = {
    'default': dj_database_url.config(default='postgresql://neondb_owner:npg_7FKjXwl6qfBE@ep-proud-sunset-a80gtoa2-pooler.eastus2.azure.neon.tech/neondb?sslmode=require')
}


CELERY_BROKER_URL = 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",
        "TIMEOUT": 60 * 10,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}