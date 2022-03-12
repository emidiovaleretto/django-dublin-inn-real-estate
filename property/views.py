from django.shortcuts import render

# Create your views here.

def property_view(request):
    return render(request, 'properties.html')

def property_detail(request):
    return render(request, 'property_inner.html')