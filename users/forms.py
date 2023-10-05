from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Form to create a new user
class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'birthdate')

# For to update a user
class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
