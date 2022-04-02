from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='book_a_viewing'),
    path('appointment/', views.schedule_a_property_viewing, name='appointment'),
]
