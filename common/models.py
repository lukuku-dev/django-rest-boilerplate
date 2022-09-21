from model_utils.models import TimeStampedModel as BaseTimeStampedModel
from django.utils import timezone
from django.db import models


class TimeStampedModel(BaseTimeStampedModel):

    @property
    def localized_created(self):
        return timezone.localtime(self.created)

    @property
    def current_timezone(self):
        return timezone.get_current_timezone()

    class Meta:
        abstract = True

class IsActiveModel(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
