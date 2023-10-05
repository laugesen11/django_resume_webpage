from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Skillset

# Set up mixin to simplify things
class SetUpMixin(LoginRequiredMixin):
    login_url = 'login'
    model = Skillset
    context_object_name = 'skillset'

# Sets up the delete view
class SkillsetDeleteView(SetUpMixin, DeleteView):
    template_name = 'skillset_delete.html'
    success_url = reverse_lazy('list_skillset')

# Sets up the create view
class SkillsetCreateView(SetUpMixin, CreateView):
    template_name = 'skillset_create.html'
    fields = ('picture', 'skill', 'years', 'details')

# Sets up the update view
class SkillsetUpdateView(SetUpMixin, UpdateView):
    template_name = 'skillset_update.html'
    fields = ('picture', 'skill', 'years', 'details')

# Sets up the list view
class SkillsetListView(ListView):
    context_object_name = 'skillsets'
    model = Skillset
    template_name = 'skillset_list.html'
