from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import filters

from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication





class LoginViewSet(ViewSet):
    
    def create(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        
        user=User.objects.filter(username=username).exists() #return boolean
        if user:
            user=User.objects.get(username=username)
            if user.check_password(password):
                #password_valid
                token=AccessToken.for_user(user)
                token=str(token)
                data={
                    'status':True,
                    'message':'login success',
                    'token':token,
                }
                return Response(data)
                
            else:
                data={
                    'status':False,
                    'message':'password not valid'
                }
                return Response(data)
                
        else:
            data={
                'status':False,
                'message':'user not found'
            }
            return Response(data)



class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields=['name','color']
    
    
    
    
    def list(self, request, *args, **kwargs):
        # self.get_queryset()
        # self.get_serializer()
        # self.filter_queryset()
        # self.paginte_queryset()
        
        # querset=Car.objects.all()  # 
        
        user=request.user #get user from request
        user=user.id
        
        
        querset=self.get_queryset().filter(created_by=user.id)


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
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    
    
    
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