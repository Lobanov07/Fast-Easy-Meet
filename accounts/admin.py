from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'date_of_birth', 'profile_picture', 'phone_number', 'preparation_time', 'created_at')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'date_of_birth', 'profile_picture', 'phone_number', 'preparation_time')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
