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

from .Property import Property
from .County import County
from .District import District
from .Neighborhood import Neighborhood
from .PropertyViewing import PropertyViewing