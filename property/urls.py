from django.urls import path
from . import views


urlpatterns = [
    path('', views.property_view, name='property_view'),
    path('property_detail/', views.property_detail, name='property_detail'),
]
