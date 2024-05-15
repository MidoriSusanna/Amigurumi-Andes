from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, EventJoin


class EventAdmin(SummernoteModelAdmin):
    """ Shows in the admin panel which user is participating in which
    event directly in the admin interface """
    summernote_fields = ('description',)
    list_display = ['name', 'location', 'date_time', 'description']


admin.site.register(Event, EventAdmin)
admin.site.register(EventJoin)

