from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.index,name='index'),
    path('project/project/', views.project, name = "project"),
    path('search/', views.search_project, name='search'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path("project/<int:project_id>/", views.project_details, name="project_details"),
    path("rate/<int:id>",views.rate, name='rate'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/',views.ProfileList.as_view()),
]