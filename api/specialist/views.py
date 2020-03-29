from django.shortcuts import render
from .models import Specialist
from .serializers import SpecialistSerialize
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerialize

    def list(self, request, *args, **kwargs):
        specialist = Specialist.objects.all()
        serialize = SpecialistSerialize(specialist, many=True)
        return Response(serialize.data)
