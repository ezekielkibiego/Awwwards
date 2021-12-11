from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile,name='index'),
    
    path('pro/project/', views.pro, name = "pro"),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    
]