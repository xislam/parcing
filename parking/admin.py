from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from parking.forms import MyUserCreationForm, MyUserChangeForm
from parking.models import Parking, Profile


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = Profile
    list_display = ['username', 'role']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )  # this will allow to change these fields in admin module


admin.site.register(Profile, MyUserAdmin)
admin.site.register(Parking)
