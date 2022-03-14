from property.models import *


class Property(models.Model):
    property_name = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    propert_address = models.CharField(null=False, max_length=255)
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    county = models.ForeignKey(County, on_delete=models.DO_NOTHING)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    property_category = models.IntegerField(
        choices=PROPERTY_CATEGORY, default=2)
    property_type = models.IntegerField(choices=PROPERTY_TYPE, default=1)
    property_price = models.IntegerField()
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
        return self.property_name                        
        
