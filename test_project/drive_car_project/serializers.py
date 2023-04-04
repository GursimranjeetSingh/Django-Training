from .models import Car,Driver

from rest_framework import serializers

from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'
        
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        
        
        
class DriverSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField()
    small_name=serializers.SerializerMethodField()
    # car=serializers.CharField(source='car.name') #gives single field
    car=CarSerializer()  #gives entire data
    simple=serializers.CharField(default='simple')
    
    
    def get_name(self,obj):
        name=obj.name
        name=name.upper()
        return name
    
    def get_small_name(self,obj):
        name=obj.name
        name=name.lower()
        return name
    
    class Meta:
        model=Driver
        fields='__all__'
        # fields=['name','age','car']
        extra_fields=['small_name','simple']
        # exclude=['age']