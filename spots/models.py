from django.db import models
from geopy.geocoders import Nominatim
from django.core.urlresolvers import reverse
from djgeojson.fields import PointField

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000,blank=True,null=True)
    def get_absolute_url(self):
        return reverse("home")
    def __str__(self):
        return self.name

class Verein(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000,blank=True,null=True)
    def get_absolute_url(self):
        return reverse("home")
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    lat = models.FloatField(blank=True,null=True)
    lon = models.FloatField(blank=True,null=True)
    datum = models.DateField(blank=True,null=True)
    desc = models.TextField(max_length=1000,blank=True,null=True)
    def save(self, *args, **kwargs):
        self.lon = Nominatim().geocode(str(self.location)).longitude
        self.lat = Nominatim().geocode(str(self.location)).latitude
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("home")
    def __str__(self):
        return self.name

class Buddy(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    ort = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000,blank=True,null=True)
    def get_absolute_url(self):
        return reverse("home")
    def __str__(self):
        return self.fname + " " + self.lname
