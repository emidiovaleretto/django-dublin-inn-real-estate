from django.urls import path
from . import views


urlpatterns = [
    path('', views.PropertyList.as_view(), name='properties'),
    path('<slug:slug>/', views.PropertyView.as_view(), name='property_detail'),
]
