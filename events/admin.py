from django.contrib import admin

# Register your models here.
from .models import Event, User, Venue

admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Event)