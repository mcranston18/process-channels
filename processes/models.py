from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings

from channels import Group


class Process(models.Model):
    name = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Process, dispatch_uid="process_saved")
def send_message(sender, instance, **kwargs):
    """
    after the process instance is saved, send a message to its user
    """
    print('sending message... ')
    Group("chat").send({
        "text": "process was saved!",
    })
