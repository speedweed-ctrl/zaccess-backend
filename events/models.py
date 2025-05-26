from django.db import models
from services.models import Service

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="events")
   

    def __str__(self):
        return self.title