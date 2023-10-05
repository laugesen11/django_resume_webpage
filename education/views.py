from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Education

# The set up mixin to simplify things
class SetUpMixin(LoginRequiredMixin):
    # Model we're using
    model = Education

    # Default context object name to access in templates
    context_object_name = 'education'
   
    # The login URL the LoginRequiredMixin redirects to
    login_url = 'login'

class CreateEducationView(SetUpMixin, CreateView):
    # The template we use in this view
    template_name = 'create_education.html'

    # The fields available to set in creation
    fields = ['picture', 'achievement', 'institution', 'date_achieved', 'valid_until']

class UpdateEducationView(SetUpMixin, UpdateView):
    # The template we use in this view
    template_name = 'update_education.html'

    # The fields available to update
    fields = ['picture', 'achievement', 'institution', 'date_achieved', 'valid_until']
   
class DeleteEducationView(SetUpMixin, DeleteView):
    # The template we use in this view
    template_name = 'delete_education.html'

    # The URL we return upon successful deletion
    success_url = reverse_lazy('list_education')

class ListEducationView(ListView):
    # The template we use in this view
    template_name = 'list_education.html'

    # Model we're using in this view
    model = Education

    # The context in which we access these objects in the template
    context_object_name = 'educations'
