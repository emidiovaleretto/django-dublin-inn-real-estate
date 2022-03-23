from django.contrib import admin
from .models import *
from user.models import Profile


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_name',)}
    list_filter = (
        'county',
        'district',
        'neighborhood',
        'property_category',
        'property_type',
    )
    list_display = (
        'property_name',
        'county',
        'district',
        'neighborhood',
        'property_category',
        'property_type',
        'property_price',
    )


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'district',)
    search_fields = ('name',)
    list_filter = ('district',)


admin.site.register(Profile)
admin.site.register(County)
admin.site.register(District)
admin.site.register(Image)
admin.site.register(PropertyViewing)
admin.site.register(PropertyViewingDate)
admin.site.register(PropertyViewingTime)
