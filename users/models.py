from django.contrib.auth.models import AbstractUser
from common.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    pass