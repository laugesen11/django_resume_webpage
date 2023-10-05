from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser

# Create a custom admin user from the CustomUser class
class CustomAdminUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserUpdateForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'birthdate']

# Register your models here.
admin.site.register(CustomUser, CustomAdminUser)
