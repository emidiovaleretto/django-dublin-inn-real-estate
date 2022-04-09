from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/edit/<slug:slug>',
         views.edit_property,
         name='edit_property'),
]
