from django.shortcuts import render

# Create your views here.

def book_a_viewing(request, property_id):
    return render(request, 'schedule-visit.html')