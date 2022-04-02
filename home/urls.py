from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('searching/', views.property_searching, name='property-searching'),
]
