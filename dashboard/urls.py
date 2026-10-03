from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
]