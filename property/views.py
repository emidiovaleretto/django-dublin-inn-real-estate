from django.shortcuts import render

# Create your views here.

def property_view(request):
    return render(request, 'properties.html')