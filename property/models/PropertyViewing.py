from property.models import *


class PropertyViewing(models.Model):
    property = models.ForeignKey(Property, null=True, related_name='property', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    day_for_viewing = models.CharField(max_length=20)
    time_for_viewing = models.TimeField()
    status = models.IntegerField(choices=VIEWING_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    