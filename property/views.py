from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from user.models import Profile


def property_list(request):
    ''' This function is used to retrieve all
    the properties from the database and render
    them on the property_list.html page '''

    properties = Property.objects.order_by('-created_at')
    paginator = Paginator(properties, 5)
    page = request.GET.get('page')
    per_page = paginator.get_page(page)

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    context = {
        'profile': profile,
        'properties': per_page,
        'pagination': per_page,
    }

    if not properties.exists():
        return render(request, '404.html', context=context)
        
    return render(request, 'properties.html', context=context)


def property_detail(request, slug):
    ''' This function display the details of
    a property as per the user choice '''

    property = get_object_or_404(Property.objects.filter(slug=slug))
    suggestions = Property.objects.exclude(slug=slug)[:2]

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    context = {
        'property': property,
        'profile': profile,
        'suggestions': suggestions
    }

    return render(request, 'property_inner.html', context=context)
