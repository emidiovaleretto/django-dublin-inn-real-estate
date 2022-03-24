from django.urls import path
from . import views


urlpatterns = [
    path('booking-a-viewing/', views.BookAPropertyViewing.as_view(), name='book_a_viewing'),
]
