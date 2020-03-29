from django.shortcuts import render
from .models import Doctor
from rest_framework import serializers


# Create your views here.

class DoctorSerialize(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'doctor_name', 'doctor_address', 'id_specialist']
