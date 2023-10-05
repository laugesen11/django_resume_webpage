from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Display, CodeLinks

# Views for handling Displays
class SetUpMixinDisplay(LoginRequiredMixin):
    # The model we will use
    model = Display

    # The context object name we will access in templates
    context_object_name = 'display'

    # The login URL the LoginRequiredMixin redirects to
    login_url = 'login'

class CreateDisplayView(SetUpMixinDisplay, CreateView):
    # The template this view returns
    template_name = 'display_create.html'
    
    # The fields available in this view
    fields = ['title', 'picture', 'details']

class UpdateDisplayField(SetUpMixinDisplay, UpdateView):
    # The template this view returns
    template_name = 'display_edit.html'

    # The fields available in this view
    fields = ['title', 'picture', 'details']

class DeleteDisplayView(SetUpMixinDisplay, DeleteView):
    # The template this view returns
    template_name = 'display_delete.html'

    # URL we return when this view suceeds
    success_url = reverse_lazy('list_display')

class ListDisplayView(ListView):
    model = Display

    # The template this view returns
    template_name = 'display_list.html'

    # The context object name we will access in templates
    context_object_name = 'displays'

class SetUpMixinCodeLinks(LoginRequiredMixin):
    # The model we will use
    model = CodeLinks

    # The context object name we will access in templates
    context_object_name = 'code_link'

    # The login URL the LoginRequiredMixin redirects to
    login_url = 'login'

class CreateCodeLinkView(SetUpMixinCodeLinks, CreateView):
    # The template this view returns
    template_name = 'code_link_create.html'

    # The fields available in this view
    fields = ['link_url', 'info', 'display']

class UpdateCodeLinkView(SetUpMixinCodeLinks, UpdateView):
    # The template this view returns
    template_name = 'code_link_update.html'

    # The fields available in this view
    fields = ['link_url', 'info', 'display']

class DeleteCodeLinkView(SetUpMixinCodeLinks, DeleteView):
    # The template this view returns
    template_name = 'code_link_delete.html'

    # URL we return when this view suceeds
    success_url = reverse_lazy('list_display')
