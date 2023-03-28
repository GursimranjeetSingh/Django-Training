from django.db import models

# Create your models here.


class Car(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,unique=True)
    car_color=models.CharField(max_length=100,default='red')    
    price=models.IntegerField(default=10000)
    company=models.CharField(max_length=100,default='company')
    four_wheel=models.BooleanField(default=True)
    mileage=models.IntegerField(default=1000)
    text_sample=models.TextField(default='text sample')
    lights=models.BooleanField(default=True)
    
    relase_date=models.DateField(default='2021-01-01')
    realease_time=models.TimeField(default='00:00:00')
    datetieme=models.DateTimeField(default='2021-01-01 00:00:00')
    
    class Meta:
        ordering=['-name','-car_color']
        
    def __str__(self):
        return self.car_color
    
    

class Driver(models.Model):
    name=models.CharField(max_length=100)
    car=models.ForeignKey(Car,on_delete=models.DO_NOTHING,)
    age=models.IntegerField(default=20)
    license_number=models.IntegerField(default=123456789)
    license_valid=models.BooleanField(default=True)
    license_valid_date=models.DateField(default='2021-01-01')
    license_valid_time=models.TimeField(default='00:00:00')
    license_valid_datetime=models.DateTimeField(default='2021-01-01 00:00:00')
    
    

class Bike(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100,blank=True,null=True)
    model=models.CharField(max_length=100,blank=True,null=True)
    


    
#models.Cascade