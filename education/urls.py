from django.urls import path
from .views import (
    CreateEducationView,
    DeleteEducationView,
    UpdateEducationView,
    ListEducationView,
)

urlpatterns = [
    path('', ListEducationView.as_view(), name='list_education'),
    path('create/', CreateEducationView.as_view(), name='create_education'),
    path('update/<int:pk>/', UpdateEducationView.as_view(), name='update_education'),
    path('delete/<int:pk>/', DeleteEducationView.as_view(), name='delete_education'),
]
