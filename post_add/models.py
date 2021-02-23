from datetime import datetime

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers
from versatileimagefield.fields import VersatileImageField, PPOIField




TYPE_BIKES=[('Scooter','Scooter'),('Bikes','Bikes')]
SIZES=[('xs','xs'),('s','s'),('m','m'),('l','l'),('xl','xl')]
TYPES=[('T-Shirt','T-Shirt'),('Polo','Polo'),('Shirt','Shirt'),('Jeans','Jeans'),('Trouser & Shorts','Trouser & Shorts'),('Tops','Tops'),('Kurtha','Kurtha'),('Saries','Saries'),('Dress & Skirt','Dress & Skirt'),('Coat & Suits','Coat & Suits'),('Hoodie & Sweetshirt','Hoodie & Sweetshirt'),('Sport & Gym','Sport & Gym'),('Undergarments','Undergarments'),('Others','Others')]
WEAR_FOR=[('Male','Male'),('Female','Female'),('Children','Children'),('Adult','Adult'),('Old People','Old People')]

HOME_DELEVERY=[('YES','YES'),('NO','NO')]
class PostAdd_Car(models.Model):
   # username= models.ForeignKey(User,on_delete=models.CASCADE)
   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)
   name = models.CharField(max_length=255, blank=True)




   image=models.ImageField(default="")
   description = models.CharField(max_length=255, blank=True)
   price=models.CharField(max_length=255,blank=True)
   lot=models.CharField(max_length=255,blank=True)
   color=models.CharField(max_length=255,blank=True)
   engine=models.CharField(max_length=255,blank=True)
   milage=models.CharField(max_length=255,blank=True)
   kilometers=models.CharField(max_length=255,blank=True)
   home_delivery=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   delivery_area=models.CharField(max_length=255,blank=True)
   warrenty=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   warrenty_period=models.CharField(max_length=255,blank=True)
   contact = models.CharField(max_length=255,blank=True)

   created_at = models.DateTimeField(auto_now_add=True)




class PostAdd_Bikes(models.Model):

   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)
   name = models.CharField(max_length=255, blank=True)



   image=models.ImageField(default="",blank=True)
   type = models.CharField(max_length=255,blank=True,choices=TYPE_BIKES)
   description = models.CharField(max_length=255, blank=True)
   usedFor = models.CharField(max_length=255,blank=True)
   price=models.CharField(max_length=255,blank=True)
   lot=models.CharField(max_length=255,blank=True)
   color=models.CharField(max_length=255,blank=True)
   engine=models.CharField(max_length=255,blank=True)
   milage=models.CharField(max_length=255,blank=True)
   kilometers=models.CharField(max_length=255,blank=True)
   home_delivery=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   delivery_area=models.CharField(max_length=255,blank=True)
   warrenty=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   warrenty_period=models.CharField(max_length=255,blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   contact = models.CharField(max_length=255,blank=True)



class PostAdd_Computer(models.Model):

   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)
   name = models.CharField(max_length=255, blank=True)



   image=models.ImageField(default="")
   description = models.CharField(max_length=255, blank=True)
   usedFor = models.CharField(blank=True,max_length=255)
   price=models.CharField(max_length=255,blank=True)
   processor=models.CharField(max_length=255,blank=True)
   ram=models.CharField(max_length=255,blank=True)
   videocard=models.CharField(max_length=255,blank=True)
   hdd=models.CharField(max_length=255,blank=True)
   screenType=models.CharField(max_length=255,blank=True)
   screenSize = models.CharField(max_length=255, blank=True)
   battery = models.CharField(max_length=255, blank=True)
   home_delivery=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   delivery_area=models.CharField(max_length=255,blank=True)
   warrenty=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   warrenty_period=models.CharField(max_length=255,blank=True)
   contact = models.CharField(max_length=255, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)


class PostAdd_Fashion(models.Model):

   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)
   name = models.CharField(max_length=255, blank=True)



   image=models.ImageField(default="")
   description = models.CharField(max_length=255, blank=True)
   usedFor = models.CharField(blank=True,max_length=255)
   price=models.CharField(max_length=255,blank=True)
   wearFor=models.CharField(max_length=255,blank=True)
   color=models.CharField(max_length=255,blank=True)
   type=models.CharField(max_length=255,blank=True,choices=TYPES)
   size=models.CharField(max_length=255,blank=True,choices=SIZES)
   home_delivery=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   delivery_area=models.CharField(max_length=255,blank=True)
   warrenty=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   warrenty_period=models.CharField(max_length=255,blank=True)
   contact = models.CharField(max_length=255,blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

class PostAdd_LandHouse(models.Model):

   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)
   name = models.CharField(max_length=255, blank=True)



   image=models.ImageField(default="")
   description = models.CharField(max_length=255, blank=True)
   price=models.CharField(max_length=255,blank=True)
   location=models.CharField(max_length=255,blank=True)
   propertyType=models.CharField(max_length=255,blank=True)
   landSize=models.CharField(max_length=255,blank=True)
   roadSize=models.CharField(max_length=255,blank=True)
   floor=models.CharField(max_length=255,blank=True)

   builtUp=models.CharField(max_length=6,blank=True)
   livingRoom=models.CharField(max_length=255,blank=True)
   bedroom = models.CharField(max_length=255, blank=True,default='')
   bathroom=models.CharField(max_length=6,blank=True)
   furnishing=models.CharField(max_length=255,blank=True)
   extraFeatures = models.CharField(max_length=255,blank=True)
   contact = models.CharField(max_length=255, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)

class PostAdd_Phones(models.Model):
   name = models.CharField(max_length=255, blank=True)

   username=models.CharField(max_length=255,default='dsfsdfdsfds',null=True,blank=True)



   image=models.ImageField(default="")
   description = models.CharField(max_length=255, blank=True)
   price=models.CharField(max_length=255,blank=True)
   usedFor=models.CharField(max_length=255,blank=True)
   screenSize=models.CharField(max_length=255,blank=True)
   sim=models.CharField(max_length=255,blank=True)
   ram=models.CharField(max_length=255,blank=True)
   backCamera=models.CharField(max_length=255,blank=True)
   CPUcore = models.CharField(max_length=255, blank=True)
   internalStorage = models.CharField(max_length=255, blank=True)
   battery = models.CharField(max_length=255, blank=True)
   home_delivery=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   delivery_area=models.CharField(max_length=255,blank=True)
   warrenty=models.CharField(max_length=6,choices=HOME_DELEVERY,blank=True)
   warrenty_period=models.CharField(max_length=255,blank=True)
   contact = models.CharField(max_length=255, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)



class PostAdvertise(models.Model):
   Add1=models.ImageField(default="")
   Add2 = models.ImageField(default="")
   Add3=models.ImageField(default="")


