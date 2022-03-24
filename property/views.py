from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import *


class PropertyList(generic.ListView):
    model = Property
    queryset = model.objects.order_by('-created_at')
    template_name = 'properties.html'
    paginate_by = 5


class PropertyView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Property.objects.filter(slug=slug)
        property = get_object_or_404(queryset)
        suggestions = Property.objects.exclude(slug=slug)[:2]
        context = {
            'property': property,
            'suggestions': suggestions
        }

        return render(request, 'property_inner.html', context=context)