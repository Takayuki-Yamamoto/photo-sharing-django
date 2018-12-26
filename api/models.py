from django.db import models


class PhotoUrl(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.url