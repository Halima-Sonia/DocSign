from django.urls import path

from . import views


urlpatterns = [

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'signup/',
        views.signup_view,
        name='signup'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

# Patient Profile
    path(
        'profile/',
        views.patient_profile,
        name='patient_profile'
    ),

    path(
        'profile/create/',
        views.create_patient_profile,
        name='create_patient_profile'
    ),

    path(
        'profile/edit/',
        views.edit_patient_profile,
        name='edit_patient_profile'
    ),

    path(
        'profile/delete/',
        views.delete_patient_profile,
        name='delete_patient_profile'
    ),
]