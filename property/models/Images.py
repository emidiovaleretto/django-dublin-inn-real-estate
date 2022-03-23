from property.models import *


class Image(models.Model):
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.image.url
    