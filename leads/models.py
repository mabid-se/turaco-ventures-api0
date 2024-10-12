from django.db import models


# Create your models here.
class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_number = models.CharField(max_length=15)
    name = models.CharField(max_length=255, blank=True)
    persons = models.CharField(max_length=255, blank=True)
    follow_up = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    destination = models.CharField(max_length=255, blank=True)
    dates = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    details = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name or 'No Name'} ({self.contact_number})"
