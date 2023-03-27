from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Car
from .serializer import CarSerializer

from django.db.models import Q



class TestViewSet(ViewSet):
    #get
    def list(self,request):
        # cars=Car.objects.all() many=True
        # cars=Car.objects.filter(id=1)
        # cars=Car.objects.filter(id__gt=1)
        # cars=Car.objects.filter(id__gt=1,name='car1',car_color='red')
        # cars=Car.objects.filter(Q(name='car1')|Q(car_color='red'))
        # cars=Car.objects.filter(id__gte=1)
        # cars=Car.objects.filter(id__lt=1)
        # cars=Car.objects.filter(id__lte=1)
        # cars=Car.objects.filter(id__in=[1,2,3])
        # cars=Car.objects.filter(id__range=[1,50])
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name')
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name').values('name')
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name').values_list('name','car_color')
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name').values_list('name',flat=True)
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name').values_list('name',flat=True).distinct()
        # cars=Car.objects.filter(id__range=[1,50]).order_by('-name').values_list('name',flat=True).distinct().count()
        cars=Car.objects.get(id=2)  #many=False
        
        
        
        cars=CarSerializer(cars)
        return Response(cars.data)
        
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
    
    
    
    
    



    





