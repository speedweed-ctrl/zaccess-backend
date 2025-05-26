from rest_framework import serializers
from .models import Reservation, Service


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id', 'title', 'description', 'start_date', 'end_date', 'service',
            'full_name', 'email', 'phone_number', 'address','amount'
        ]
