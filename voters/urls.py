from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index ,name = 'index'),
    path('FAQ/',views.FAQ ,name = 'FAQ'),
    path('accounts/profile/', views.index,name='index'),
    path('profile/',views.profile,name = 'profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
]