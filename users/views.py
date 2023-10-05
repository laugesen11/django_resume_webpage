from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# View for the creation of a new user
class UserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
