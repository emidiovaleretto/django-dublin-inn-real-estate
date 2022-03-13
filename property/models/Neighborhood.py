from property.models import *


class Neighborhood(models.Model):
    name = models.CharField(null=False, max_length=50)
    district = models.ForeignKey(District, null=True, related_name='district', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    