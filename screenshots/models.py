from __future__ import unicode_literals
from django.db import models


class TimeStampModel(models.Model):
    added_date = models.DateTimeField(auto_now_add = True,editable=True)
    modified_date = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Website(TimeStampModel):
    link = models.CharField(max_length=255)
    screenshot = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.link
