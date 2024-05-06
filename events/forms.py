from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'date_time', 'description']

class ParticipationForm(forms.Form):
    """ Handle the ID of an event in which a user wants to join.
    Uses HiddenInput widget so that data is not changed by users manually"""
    event_id = forms.IntegerField(widget=forms.HiddenInput())