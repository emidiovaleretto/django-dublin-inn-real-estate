from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from property.models import PropertyViewing
from user.models import Profile


@login_required(login_url='/auth/login')
def my_scheduled_visits(request):
    ''' This function is responsible for
    rendering the page with the list
    of scheduled visits '''

    user = request.user
    appointments = PropertyViewing.objects.filter(user=user)
    paginator = Paginator(appointments, 5)
    page = request.GET.get('page')
    per_page = paginator.get_page(page)

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    context = {
        'appointments': per_page,
        'pagination': per_page,
        'profile': profile
    }

    return render(request, 'my-scheduled-visits.html', context=context)


def cancellation(request, id):
    ''' This function cancels the scheduled visit
    and redirects to the my scheduled visits page '''

    viewing = get_object_or_404(PropertyViewing, id=id)
    viewing.status = 2
    viewing.save()
    return redirect('my-scheduled-visits')
