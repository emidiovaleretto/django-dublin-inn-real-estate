from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from user.models import Profile


def property_list(request):
    properties = Property.objects.order_by('-created_at')
    profile = get_object_or_404(Profile.objects.all())
    paginator = Paginator(properties, 5)
    page = request.GET.get('page')
    per_page = paginator.get_page(page)

    context = {
        'properties': per_page,
        'profile': profile
    }

    return render(request, 'properties.html', context=context)


def property_detail(request, slug):
    property = get_object_or_404(Property.objects.filter(slug=slug))
    profile = get_object_or_404(Profile.objects.all())
    suggestions = Property.objects.exclude(slug=slug)[:2]
    context = {
        'property': property,
        'profile': profile,
        'suggestions': suggestions
    }

    return render(request, 'property_inner.html', context=context)
