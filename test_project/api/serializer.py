from rest_framework import serializers
from .models import Car,Bike, A, B



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'
        
        
class BikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Bike
        # fields='__all__'
        fields=['name','color','model']
        # exclude=['id']
    
    
    
    
class ASerializer(serializers.ModelSerializer):
    class Meta:
        model=A
        fields='__all__'
        

class BSerializer(serializers.ModelSerializer):
    class Meta:
        model=B
        fields='__all__'