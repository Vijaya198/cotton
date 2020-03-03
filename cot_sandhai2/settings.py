import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cot_sandhai2.settings")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kk*j#u(2dpw8+c&tx@3fa$gw_0o@=rz5-jk!7w_04(xv^euqct'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
WSGI_APPLICATION = 'cot_sandhai2.wsgi.application'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'account_login',

    #'AccountLogin.apps.AccountLoginConfig'
    'trade_information',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',



]
#ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

SITE_ID = 0

ACCOUNT_AUTHENTICATION_METHOD="email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


LOGIN_REDIRECT_URL = "/traderadd"


#EMAIL_SUBJECT_PREFIX = '[dev user skeleton] '

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'example@gmail.com'

#EMAIL_HOST_PASSWORD = 'examplepwd'
#EMAIL_USE_TLS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'account_login.middleware.OneSessionPerUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cot_sandhai2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]
AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',


    'allauth.account.auth_backends.AuthenticationBackend',



)




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME':'cotton_sandhai',
        'NAME':'cot_sandhai2',
        #'USER':'admin',
        'USER':'root',
       # 'PASSWORD':'VRgeeks123',
        'PASSWORD':'Kanishka07052010',
        #'HOST':'database-1.cg2nmqihdd66.ap-south-1.rds.amazonaws.com',
        'HOST':'localhost',
        'PORT':'3306',
        #'OPTIONS': {
        #   'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
       # }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    },
    'google': {
        'SCOPE': [
           'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False



ACCOUNT_LOGOUT_ON_GET = True

#AUTH_USER_MODEL = 'account_login.User'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'umadevi.suren@gmail.com'
EMAIL_HOST_PASSWORD = 'pifuizzkficciywa'
PASSWORD_RESET_TIMEOUT_DAYS=1
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SOCIAL_AUTH_LOGIN_URL = 'accounts/login'
SOCIAL_AUTH_LOGOUT_URL = 'user_logout'
#SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/traderadd'
#FACEBOOK_APP_ID = str('176266560136878')
#FACEBOOK_APP_SECRET = str('ece90495c8d172913c603746a920bb28')

#AUTH_USER_MODEL ='account_login.User'
