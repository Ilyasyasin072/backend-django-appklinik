from django.db import models
from api.specialist.models import Specialist


# Create your models here.
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=10)
    doctor_address = models.CharField(max_length=100)
    id_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
