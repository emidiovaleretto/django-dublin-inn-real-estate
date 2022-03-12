from django.urls import path
from . import views


urlpatterns = [
    path('property-id=<int:property_id>', views.book_a_viewing, name='book_a_viewing'),
]
