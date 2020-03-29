from rest_framework import serializers
from .models import Patient


class PatientSerialize(serializers.ModelSerializer):
    class Meta:
        patient = Patient
        field = ['id', 'patient_name', 'patient_address', 'patient_phone', 'patient_KTP']


class PatientMiniSerialize(serializers.ModelSerializer):
    class Meta:
        patient = Patient
        field = ['id', 'patient_name', 'patient_address', 'patient_phone', 'patient_KTP']
