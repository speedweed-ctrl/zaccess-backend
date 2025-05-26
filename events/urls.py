from django.urls import path
from .views import (
    ServiceListAPIView,
    EventListCreateAPIView,
    EventDetailAPIView,
)

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('', EventListCreateAPIView.as_view(), name='reservation-list-create'),
    path('event/<int:pk>/', EventDetailAPIView.as_view(), name='reservation-detail'),
]
