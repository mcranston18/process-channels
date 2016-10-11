from django.db import models
from django.conf import settings


class Process(models.Model):
    name = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
