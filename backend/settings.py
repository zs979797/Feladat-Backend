import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'your_secret_key'
DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['rest_framework', 'corsheaders', 'tasks']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware']
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'feladat_db', 'USER': 'postgres', 'PASSWORD': 'yourpassword', 'HOST': '127.0.0.1', 'PORT': '5432' } }
WSGI_APPLICATION = 'backend.wsgi.application'