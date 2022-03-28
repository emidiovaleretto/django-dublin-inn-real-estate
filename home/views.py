from django.shortcuts import render, get_object_or_404
from django.views import generic
from property.models import Property
from user.models import Profile


class HomeView(generic.ListView):

    def get(self, request, *args, **kwargs):
        properties = Property.objects.all()[:3]
        profile = get_object_or_404(Profile.objects.all())

        context = {
            'properties': properties,
            'profile': profile
        }

        return render(request, 'index.html', context=context)
