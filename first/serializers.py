from rest_framework import serializers
from .models import InfectedPlace

class InfectedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectedPlace
        fields = ('name', 'address', 'lat', 'lng', 'created_at', 'updated_at', 'memo')