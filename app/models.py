from django.db import models

from datetime import datetime

class PhotoUrl(models.Model):
    cloud_id =models.CharField(verbose_name='cloud_id', max_length=128)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.cloud_id