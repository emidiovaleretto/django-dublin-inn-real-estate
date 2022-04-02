from django.urls import path
from . import views


urlpatterns = [
    path('booking-a-viewing/', views.index, name='book_a_viewing'),
]
