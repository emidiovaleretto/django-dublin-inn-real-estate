from property.models import *


class Property(models.Model):
    slug = models.SlugField(max_length=100, null=False, unique=True)
    property_name = models.CharField(max_length=50, null=False, unique=True)
    propert_address = models.CharField(null=False, max_length=255)
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, related_name='neighborhood', on_delete=models.SET_NULL)
    district = models.ForeignKey(District, related_name='district', on_delete=models.SET_NULL)
    county = models.ForeignKey(County, related_name='county', on_delete=models.SET_NULL)
    description = models.TextField()
    images = CloudinaryField('image', default='placeholder')
    property_category = models.IntegerField(
        choices=PROPERTY_CATEGORY, default=2)
    property_type = models.IntegerField(choices=PROPERTY_TYPE, default=1)
    property_price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    metreage = models.FloatField()
    viewing_date = models.ManyToManyField(PropertyViewingDate)
    viewing_time = models.ManyToManyField(PropertyViewingTime)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name                        
        
