from django.urls import path
from .views import ServiceListCreate, ServiceDetail

urlpatterns = [
    path('service', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
]
