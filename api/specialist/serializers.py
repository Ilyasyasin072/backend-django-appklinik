from rest_framework import serializers
from .models import Specialist


class SpecialistSerialize(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'specialist_name', 'specialist_desc']
