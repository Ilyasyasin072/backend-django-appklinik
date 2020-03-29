from rest_framework import serializers
from .models import Specialist


class SpecialistSerialize(serializers.ModelSerializer):
    class Meta:
        field = ['id', 'specialist_name', 'specialist_desc']
