from django.db import models


# Create your models here.
class Specialist(models.Model):
    specialist_name = models.CharField(max_length=50)
    specialist_desc = models.CharField(max_length=100)
