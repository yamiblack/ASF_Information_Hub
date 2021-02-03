from rest_framework import serializers
from .models import InfectedPlace

class InfectedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectedPlace
        fields = ('name', 'address', 'lat', 'lng', 'happened_at', 'reported2oie_at', 'memo', 'created_at', 'updated_at')