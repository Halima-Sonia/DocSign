from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, PatientProfile


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name',
        })
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email address',
        })
    )

    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter phone number',
        })
    )

    class Meta:

        model = CustomUser

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2',
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username',
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })

    def save(self, commit=True):

        user = super().save(commit=False)

        user.role = 'patient'

        if commit:
            user.save()

        return user

from django import forms
from .models import PatientProfile


class PatientProfileForm(forms.ModelForm):

    class Meta:
        model = PatientProfile
        fields = [
            'date_of_birth',
            'gender',
            'address',
            'blood_group',
            'emergency_contact',
            'medical_history',
            'allergies',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'gender': forms.Select(
                attrs={'class': 'form-control'}
            ),

            'address': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter your address'
                }
            ),

            'blood_group': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. A+, B+, O+'
                }
            ),

            'emergency_contact': forms.TextInput(
                attrs={
                    'placeholder': 'Emergency contact number'
                }
            ),

            'medical_history': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Describe any important medical history'
                }
            ),

            'allergies': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'List any known allergies'
                }
            ),
        }