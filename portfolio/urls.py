from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]
