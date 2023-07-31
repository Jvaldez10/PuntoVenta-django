import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

POSTGRESQL = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db",
        "USER": "postgres",
        "PASSWORD": "7410",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# POSTGRESQL = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd8fiien0srjalh',
#         'USER': 'odtajsgrrvlzdy',
#         'PASSWORD': 'bf4772550c41bbb0e1ca8aed36f540f487d12608e32aacce35e446b9647b9021',
#         'HOST': 'ec2-3-219-229-143.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }
