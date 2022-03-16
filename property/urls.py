from django.urls import path
from . import views


urlpatterns = [
    path('', views.PropertyList.as_view(), name='properties'),
    path('property_detail/', views.property_detail, name='property_detail'),
]
