from django.shortcuts import render
from .serializers import PatientSerialize, PatientMiniSerialize
from .models import Patient
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerialize

    def list(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientMiniSerialize(patients, many=True)
        return Response(serializer.data)
