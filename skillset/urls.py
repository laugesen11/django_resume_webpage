from django.urls import path
from .views import (
    SkillsetCreateView,
    SkillsetUpdateView,
    SkillsetDeleteView,
    SkillsetListView,
)

urlpatterns = [
    path('', SkillsetListView.as_view(), name='list_skillset'),
    path('create/', SkillsetCreateView.as_view(), name='create_skillset'),
    path('delete/<int:pk>/', SkillsetDeleteView.as_view(), name='delete_skillset'),
    path('update/<int:pk>/', SkillsetUpdateView.as_view(), name='update_skillset'),
]
