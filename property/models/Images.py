from property.models import *


class Image(models.Model):
    image = CloudinaryField('image', default='placeholder')
