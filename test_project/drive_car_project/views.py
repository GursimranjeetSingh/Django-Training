from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from rest_framework.response import Response



class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    
    
class DriverViewSet(ModelViewSet):
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    
    
    @action(detail=False,methods=['get'])
    def get_driver_car_name(self,request):
        driver_name=request.query_params.get('driver_name')
        # driver_name=request.GET.get('driver_name')
        driver_car=Driver.objects.filter(name=driver_name).values_list('car__name',flat=True)
        driver_car=driver_car[0]
        data={
            'driver_name':driver_name,
            'driver_car':driver_car
        }
        return Response(data)