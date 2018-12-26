from django.db import models

from datetime import datetime

class PhotoUrl(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.url