from django.urls import path
from .views import (
    CreateDisplayView,
    UpdateDisplayField,
    DeleteDisplayView,
    ListDisplayView,
    CreateCodeLinkView,
    UpdateCodeLinkView,
    DeleteCodeLinkView,
)

urlpatterns = [
    path('', ListDisplayView.as_view(), name='list_display'),
    path('display/create/', CreateDisplayView.as_view(), name='create_display'),
    path('display/update/<int:pk>/', UpdateDisplayField.as_view(), name='update_display'),
    path('display/delete/<int:pk>', DeleteDisplayView.as_view(), name='delete_display'),
    path('codelink/create/', CreateCodeLinkView.as_view(), name='create_code_link'),
    path('codelink/delete/<int:pk>/', DeleteCodeLinkView.as_view(), name='delete_code_link'),
    path('codelink/update/<int:pk>/', UpdateCodeLinkView.as_view(), name='update_code_link'),
]
