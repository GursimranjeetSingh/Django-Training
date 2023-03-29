from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from .models import Car,Bike,A,B
from .serializer import CarSerializer,BikeSerializer,ASerializer,BSerializer

from django.db.models import Q
from rest_framework.decorators import action





        
        
    
class BViewSet(ModelViewSet):
    queryset=B.objects.all()
    serializer_class=BSerializer

class BikeViewSet(ModelViewSet):
    queryset=Bike.objects.all()
    serializer_class=BikeSerializer

        

class TestViewSet(ViewSet):
    
    #post
    def create(self,request):
        data=request.data
        serializer=CarSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        
        return Response('data created')
        
    
    #get
    def retrieve(self,request,pk=None):
        cars=Car.objects.get(id=int(pk))
        cars=CarSerializer(cars)
        return Response(cars.data)
    
    # put 
    def update(self,request,pk=None):
        data=request.data
        
        car=Car.objects.get(id=int(pk))
        
        cars_serializer=CarSerializer(car,data=data)
        cars_serializer.is_valid(raise_exception=True)
        cars_serializer.save()
        
        
        return Response({'test':'test'})
    
    #delete
    def destroy(self,request,pk=None):
        pk=int(pk)
        # Car.objects.get(id=pk).delete() #delete generates error
        # Car.objects.filter(id=pk).delete() #delete will not generate error
        return Response('deleted')


    #patch
    def partial_update(self,request,pk=None):
        data=request.data
        
        car=Car.objects.get(id=int(pk))
        
        cars_serializer=CarSerializer(car,data=data,partial=True)
        cars_serializer.is_valid(raise_exception=True)
        cars_serializer.save()
        
        
        return Response({'test':'test'})
    
    
    
    
    



    





