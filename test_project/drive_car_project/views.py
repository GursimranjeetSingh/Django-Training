from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import filters





class LoginViewSet(ViewSet):
    
    def list(self,request):
        return Response({'data':'login'})



class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['name','color']
    
    
    def list(self, request, *args, **kwargs):
        # self.get_queryset()
        # self.get_serializer()
        # self.filter_queryset()
        # self.paginte_queryset()
        
        # querset=Car.objects.all()  # 
        querset=self.get_queryset()


        queryset=self.filter_queryset(querset)
        
        # serializers=CarSerializer(queryset,many=True)
        serializers=self.get_serializer(queryset,many=True)
        
        
        
        data=serializers.data
        
        data={
            'data':data,
            'status':True,
        }
        
        return Response(data)
    
    
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
    
    
    
#search fields
#get queryset
#get serializer
# get filter backends