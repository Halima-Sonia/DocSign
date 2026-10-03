from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import PatientProfile
from .forms import SignUpForm, PatientProfileForm


@login_required
def patient_profile(request):
    profile = PatientProfile.objects.filter(
        user=request.user
    ).first()

    return render(
        request,
        'patient_profile.html',
        {'profile': profile}
    )


@login_required
def create_patient_profile(request):

    profile = PatientProfile.objects.filter(
        user=request.user
    ).first()

    if profile:
        return redirect('patient_profile')

    if request.method == 'POST':
        form = PatientProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('patient_profile')

    else:
        form = PatientProfileForm()

    return render(
        request,
        'patient_profile_form.html',
        {
            'form': form,
            'title': 'Create Patient Profile'
        }
    )


@login_required
def edit_patient_profile(request):

    profile = get_object_or_404(
        PatientProfile,
        user=request.user
    )

    if request.method == 'POST':
        form = PatientProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()

            return redirect('patient_profile')

    else:
        form = PatientProfileForm(
            instance=profile
        )

    return render(
        request,
        'patient_profile_form.html',
        {
            'form': form,
            'title': 'Edit Patient Profile'
        }
    )


@login_required
def delete_patient_profile(request):

    profile = get_object_or_404(
        PatientProfile,
        user=request.user
    )

    if request.method == 'POST':
        profile.delete()

        return redirect('patient_profile')

    return render(
        request,
        'delete_patient_profile.html',
        {'profile': profile}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(request, 'login.html')


def signup_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:

        form = SignUpForm()

    return render(
        request,
        'signup.html',
        {
            'form': form
        }
    )


def logout_view(request):

    logout(request)

    return redirect('login')