from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255)    
    address1 = models.CharField(max_length=255)    
    address2 = models.CharField(max_length=255, blank=True)    
    address3 = models.CharField(max_length=255, blank=True)    
    address4 = models.CharField(max_length=255, blank=True)    
    postcode = models.CharField(max_length=255)    


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    buildings = models.ManyToManyField(Building, related_name='organisations')
    telephone = models.CharField(max_length=30)


class Activity(models.Model):
    name = models.CharField(max_length=255)


class Room(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(Building, related_name='rooms')


class Allocation(models.Model):
    activity = models.ForeignKey(Activity, related_name='allocations')
    room = models.ForeignKey(Room, related_name='allocations')
