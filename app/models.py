from django.db import models

from datetime import datetime

from cloudinary.models import CloudinaryField


class Photo(models.Model):
    image = CloudinaryField('image')
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s>" % public_id
