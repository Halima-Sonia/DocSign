from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
    return render(request, 'contact.html')

def departments(request):
    return render(request, 'departments.html')

def services(request):
    return render(request, 'services.html')

def appointment(request):
    return render(request, 'appointment.html')
