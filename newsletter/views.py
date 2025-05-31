from rest_framework import generics
from .models import ClientMessage
from .serializers import ClientMessageSerializer

class ClientMessageListCreateView(generics.ListCreateAPIView):
    queryset = ClientMessage.objects.all()
    serializer_class = ClientMessageSerializer

class ClientMessageDeleteView(generics.DestroyAPIView):
    queryset = ClientMessage.objects.all()
    serializer_class = ClientMessageSerializer
    lookup_field = 'id'
