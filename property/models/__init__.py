from django.db import models
from django.contrib.auth.models import User


PROPERTY_CATEGORY = (
    (1, 'Sale'),
    (2, 'Rent')
)

PROPERTY_TYPE = (
    (1, 'Studio'),
    (2, 'Apartment'),
    (3, 'House')
)

from .Property import Property
from .County import County
from .District import District