from django.db import models


# Create your models here.
# Model Patient
class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_address = models.CharField(max_length=255)
    patient_phone = models.IntegerField()
    patient_KTP = models.IntegerField()
