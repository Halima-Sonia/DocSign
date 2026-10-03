from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('DocSign Information', {
            'fields': ('role', 'phone'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('DocSign Information', {
            'fields': ('role', 'phone'),
        }),
    )