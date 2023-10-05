from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    WorkExperienceCreateView,
    WorkExperienceDeleteView,
    WorkExperienceUpdateView,
    WorkExperienceListView
)

urlpatterns = [
    path('', WorkExperienceListView.as_view(), name='list_work_experiences'),
    path('create/', WorkExperienceCreateView.as_view(), name='create_work_experience'),
    path('update/<int:pk>/', WorkExperienceUpdateView.as_view(), name='update_work_experience'),
    path('delete/<int:pk>/', WorkExperienceDeleteView.as_view(), name='delete_work_experience'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
