from django.urls import path
from . import views


urlpatterns = [
    path('', views.property_view, name='property_view'),
]
