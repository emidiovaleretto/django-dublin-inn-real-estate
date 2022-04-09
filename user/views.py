from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from property.models import *
from .models import Profile


@login_required(login_url='/auth/login')
def user_profile(request):
    ''' This function returns the user profile '''
    
    username = request.user
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    profile.save()
    context = {'profile': profile}
    return render(request, 'user_profile.html', context=context)


@login_required(login_url='/auth/login')
def admin_panel(request):
    ''' This function returns the admin panel '''

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

    return render(request, 'admin_panel.html', context=context)


@login_required(login_url='/auth/login')
def edit_property(request, slug):
    ''' This function returns the edit property page '''

    property = get_object_or_404(Property.objects.filter(slug=slug))
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    else:
        profile = Profile.objects.all()

    context = {'property': property, 'profile': profile}
    return render(request, 'edit_property.html', context=context)


@login_required(login_url='auth/login')
def update_property(request, slug):
    ''' This function uptades the property content 
    and redirects to the property page details. '''

    if request.method == 'POST':
        property = get_object_or_404(Property.objects.filter(slug=slug))
        property.property_name = request.POST.get('property-name')
        property.property_address = request.POST.get('property-address')
        property.description = request.POST.get('description')
        property.property_category = request.POST.get('property-category')
        property.property_type = request.POST.get('property-type')
        property.property_price = request.POST.get('property-price')
        property.bedrooms = request.POST.get('bedrooms')
        property.bathrooms = request.POST.get('bathrooms')
        property.metreage = request.POST.get('metreage')

        property.save()

        return redirect('property_detail', property.slug)
    
    else:
        return render(request, 'edit_property.html')
