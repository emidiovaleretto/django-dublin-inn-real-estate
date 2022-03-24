from django.shortcuts import render, get_object_or_404
from django.views import generic
from property.models import Property


class HomeView(generic.ListView):
    model = Property
    queryset = model.objects.all()[:3]
    template_name = 'index.html'
