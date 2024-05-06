from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventParticipation
from .forms import EventForm, ParticipationForm

def event_list(request):
    """Display list of events"""
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def join_event(request):
    """Only authenticated users can join events, if they join they are
    redirected to my events page"""
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = Event.objects.get(id=event_id)
            EventJoin.objects.create(user=request.user, event=event)
            return redirect('my_events')
    return redirect('events')

@login_required
def leave_event(request, event_id):
    """Authneticated users can leave the events they have previously
    joined"""
    EventJoin.objects.filter(user=request.user, event_id=event_id).delete()
    return redirect('my_events')

@login_required
def my_events(request):
    """Shows the events the user has joined"""
    participations = request.user.participations.all()
    return render(request, 'events/my_events.html', {'participations': participations})
