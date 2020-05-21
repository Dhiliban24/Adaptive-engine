from config.settings.base import *
import django_heroku
import dj_database_url

SECRET_KEY = 'sp(j(ts6ri()muwz-$^i+k+jgjfv$jbgs@9oq@lzy6x5@lynqd'

INSTALLED_APPS += [
    'django_extensions',
]

ALLOWED_HOSTS += ['localhost', 'engine','127.0.0.1','*']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'engine',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    }
}
db_from_env=dj_database_url.congif(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'engine': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'alosi.engine': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },
}

