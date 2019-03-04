import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tests_db',
        'USER': 'tester',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


