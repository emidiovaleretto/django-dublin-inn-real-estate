from django.shortcuts import render, get_object_or_404
from django.views import View
from property.models import Property
from user.models import Profile


class BookAPropertyViewing(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Property.objects.filter(slug=slug)
        property = get_object_or_404(queryset)
        profile = get_object_or_404(Profile.objects.all())
        context = {
            'property': property,
            'profile': profile
        }
        return render(request, 'schedule-visit.html', context=context)
