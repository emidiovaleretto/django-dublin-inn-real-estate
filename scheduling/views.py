from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from property.models import Property
from user.models import Profile


@login_required(login_url='/auth/login')
def index(request, slug):
    property = get_object_or_404(Property, slug=slug)
    profile = get_object_or_404(Profile.objects.all())

    context = {
        'property': property,
        'profile': profile
    }
    return render(request, 'schedule-visit.html', context=context)
