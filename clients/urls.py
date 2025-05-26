from django.urls import path
from .views import ClientListCreateView, ClientDetailView

urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list-create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]
