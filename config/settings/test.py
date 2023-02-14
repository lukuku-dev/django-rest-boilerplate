from base import *
import os

"""This is the test settings file. It is used only for testing purposes.
"""

# All of the tests are performed in memory
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'}
}
