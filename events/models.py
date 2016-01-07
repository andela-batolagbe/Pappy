from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .auth import UserManager
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractBaseUser):
	username = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)

	REQUIRED_FIELDS = ['username']

	objects = UserManager()

	def get_full_name(self):
		return ''.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name

class Venue(models.Model):
	venue_name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	state = models.CharField(max_length=20)

class Event(models.Model):
	Host = models.ForeignKey(User, on_delete=models.CASCADE)
	Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
	Date = models.DateField(blank=True)
	Time = models.TimeField(blank=True)
