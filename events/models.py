from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

class Venue(models.Model):
	venue_name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	state = models.CharField(max_length=20)

class Event(models.Model):
	Host = models.ForeignKey(User, on_delete=models.CASCADE)
	Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
	Date = models.DateField(blank=True)
	Time = models.TimeField(blank=True)

