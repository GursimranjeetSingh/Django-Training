from .models import Car,Driver

from rest_framework import serializers



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'
        
        
        
        
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver
        fields='__all__'