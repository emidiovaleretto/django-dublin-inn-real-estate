from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Client'),
    (3, 'Agent')
)

from .User import Profile