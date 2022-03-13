from property.models import *


class PropertyViewingDate(models.Model):
    day_of_viewing = models.CharField(null=False, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.day_of_viewing
