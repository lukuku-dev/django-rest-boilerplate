from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    pass