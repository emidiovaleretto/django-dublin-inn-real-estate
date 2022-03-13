from property.models import *


class District(models.Model):
    name = models.CharField(null=True, max_length=50)
    county = models.ForeignKey(County, null=True, related_name='county', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.county.name}'
