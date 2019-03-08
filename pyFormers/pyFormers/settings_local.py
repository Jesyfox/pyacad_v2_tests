import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'tests_db'),
        'USER': os.getenv('POSTGRES_USER', 'tester'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123456'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', 5432)
    }
}



