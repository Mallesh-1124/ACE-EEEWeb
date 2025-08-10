# Django URL configuration for the eeeweb app
# This file defines the URL patterns for the eeeweb application.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('carrerplace/', views.carrerplace, name='careerplace'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
