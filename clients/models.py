from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to="client_images/", null=True, blank=True)

    def __str__(self):
        return self.full_name