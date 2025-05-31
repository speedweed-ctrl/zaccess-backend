from django.urls import path
from .views import ClientMessageListCreateView, ClientMessageDeleteView

urlpatterns = [
    path('messages/', ClientMessageListCreateView.as_view(), name='list-create-messages'),
    path('messages/<int:id>/', ClientMessageDeleteView.as_view(), name='delete-message'),
]