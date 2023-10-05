from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import WorkExperience

# Create your views here.
class SetUpMixin(LoginRequiredMixin):
    login_url = 'login'
    model = WorkExperience 
    context_object_name = 'work_experience'

class WorkExperienceCreateView(SetUpMixin, CreateView):
    template_name = 'work_experience_create.html'
    fields = ( 'picture', 'company', 'team_name', 'job_title', 'start_date', 'end_date', 'work', )

class WorkExperienceDeleteView(SetUpMixin, DeleteView):
    success_url = reverse_lazy('list_work_experiences')
    template_name = 'work_experience_delete.html'

class WorkExperienceUpdateView(SetUpMixin, UpdateView):
    template_name = 'work_experience_edit.html'
    fields = ( 'picture', 'company', 'team_name', 'job_title', 'start_date', 'end_date', 'work', )

class WorkExperienceListView(ListView):
    model = WorkExperience 
    context_object_name = 'work_experiences'
    template_name = 'work_experience_list.html'
