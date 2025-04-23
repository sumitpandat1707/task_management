from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture', 'address', 'birth_date', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture', 'address', 'birth_date', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

