from django.db import models

class Car(models.Model):
    name=models.CharField(max_length=100,unique=True)
    color=models.CharField(max_length=100,default='red')
    company=models.CharField(max_length=100,default='company')
    
    
class Driver(models.Model):
    name=models.CharField(max_length=100,unique=True)
    age=models.IntegerField(default=20)
    car=models.ForeignKey(Car,on_delete=models.DO_NOTHING,)
    