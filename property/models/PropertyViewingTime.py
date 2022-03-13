from property.models import *


class PropertyViewingTime(models.Model):
    time_of_viewing = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.time_of_viewing)
    