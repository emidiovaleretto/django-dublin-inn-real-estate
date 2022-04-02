from django.shortcuts import render, get_object_or_404
from property.models import PropertyViewing
from user.models import Profile


def my_scheduled_visits(request):
    user = request.user
    profile = get_object_or_404(Profile.objects.all())
    appointments = PropertyViewing.objects.filter(user=user)

    context = {
        'appointments': appointments,
        'profile': profile
    }

    return render(request, 'my-scheduled-visits.html', context=context)
