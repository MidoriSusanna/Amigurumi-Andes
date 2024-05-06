from django.contrib import admin
from .models import Event, EventJoin

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'date_time', 'description']

@admin.register(EventJoin)
class EventJoinAdmin(admin.ModelAdmin):
    """ Shows in the admin panel which user is participating in which 
    event directly in the admin interface """
    list_display = ['user', 'event']
