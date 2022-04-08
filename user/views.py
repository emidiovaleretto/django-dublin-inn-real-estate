from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


def get_user_profile(request):
    ''' This function returns the user profile '''
    username = request.GET.get('username')
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    profile.save()
    context = {'profile': profile}
    return render(request, 'profile.html', context=context)
