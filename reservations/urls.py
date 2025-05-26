from django.urls import path
from .views import (
    ServiceListAPIView,
    ReservationListCreateAPIView,
    ReservationDetailAPIView,
)

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('reservation/<int:pk>/', ReservationDetailAPIView.as_view(), name='reservation-detail'),
]
