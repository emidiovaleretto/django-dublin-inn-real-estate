from django.shortcuts import render
from django.views import generic, View
from .models import *


class PropertyList(generic.ListView):
    model = Property
    queryset = model.objects.order_by('-created_at')
    template_name = 'properties.html'
    paginate_by = 5

def property_detail(request):
    return render(request, 'property_inner.html')