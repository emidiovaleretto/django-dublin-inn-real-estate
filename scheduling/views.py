from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from property.models import Property, PropertyViewing
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


def schedule_a_property_viewing(request, slug):
    user = request.user
    appointment_date = request.POST.get('appointment-date')
    appointment_time = request.POST.get('appointment-time')
    property = get_object_or_404(Property, slug=slug)

    viewing = PropertyViewing(
        user=user,
        property=property,
        day_for_viewing=appointment_date,
        time_for_viewing=appointment_time
    )

    viewing.save()
    return redirect('my-scheduled-visits')
