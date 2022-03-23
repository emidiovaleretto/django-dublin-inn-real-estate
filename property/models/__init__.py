from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


PROPERTY_CATEGORY = (
    (1, 'Sale'),
    (2, 'Rent')
)

PROPERTY_TYPE = (
    (1, 'Studio'),
    (2, 'Apartment'),
    (3, 'House')
)

VIEWING_STATUS = (
    (1, 'Scheduled'),
    (2, 'Cancelled')
)

VIEWING_DATE = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)

from .County import County
from .District import District
from .Neighborhood import Neighborhood
from .PropertyViewingDate import PropertyViewingDate
from .PropertyViewingTime import PropertyViewingTime
from .Images import Image
from .Property import Property
from .PropertyViewing import PropertyViewing
