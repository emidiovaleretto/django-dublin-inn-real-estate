from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from property.models import Property, District, Neighborhood
from user.models import Profile


def index(request):
    properties = Property.objects.all()[:3]
    districts = District.objects.all()

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    context = {
        'properties': properties,
        'districts': districts,
        'profile': profile
    }

    return render(request, 'index.html', context=context)


def property_searching(request):
    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')
    location = request.GET.get('location')
    property_type = request.GET.get('property-type')

    if min_price or max_price or location or property_type:

        if not min_price:
            min_price = 1000
        if not max_price:
            max_price = 10000
        if not location:
            location = District.objects.all()
        if not property_type:
            property_type = [1, 2, 3]

        properties = Property.objects.filter(property_price__gte=min_price).filter(
            property_price__lte=max_price).filter(district__in=location).filter(property_type__in=property_type)

        if not properties.exists():
            # TODO Create a 404 template
            return HttpResponse('<h1>No properties available</h1>')

    else:
        properties = Property.objects.all()

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    paginator = Paginator(properties, 5)
    page = request.GET.get('page')
    per_page = paginator.get_page(page)

    context = {
        'pagination': per_page,
        'properties': per_page,
        'profile': profile
    }

    return render(request, 'properties.html', context=context)
