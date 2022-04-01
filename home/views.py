from django.shortcuts import render, get_object_or_404
from property.models import Property, District, Neighborhood
from user.models import Profile


def index(request):
    properties = Property.objects.all()[:3]
    districts = District.objects.all()
    neigborhood = Neighborhood.objects.all()
    profile = get_object_or_404(Profile.objects.all())

    context = {
        'properties': properties,
        'districts': districts,
        'neighborhoods': neigborhood,
        'profile': profile
    }

    return render(request, 'index.html', context=context)
