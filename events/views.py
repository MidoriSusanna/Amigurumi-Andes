from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Event, EventJoin
from .forms import EventForm, ParticipationForm


def event_list(request):
    """Display list of events with indication
    of participation for logged-in users."""
    events = Event.objects.all()
    user_participations = set()
    if request.user.is_authenticated:
        user_participations = set(request.user.participations.values_list(
            'event_id', flat=True))
    return render(request, 'events/event_list.html', {
        'events': events, 'user_participations': user_participations})


@login_required
def join_event(request):
    """Only authenticated users can join events, if they join they are
    redirected to my events page and receive an email confirmation."""
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = Event.objects.get(id=event_id)
            EventJoin.objects.create(user=request.user, event=event)

            # Send confirmation email
            send_mail(
                subject=f"Confirmation for joining {event.name}",
                message=f"Hi {request.user.first_name},"
                        f"\n\nYou have successfully joined "
                        f"the event '{event.name}' scheduled "
                        f"for {event.date_time}. Here are the "
                        f"details:\n\nLocation: {event.location}"
                        f"\n\nThank you for joining!",
                from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
                recipient_list=[request.user.email],
                fail_silently=False,
            )

            return redirect('my_events')
    return redirect('events')


@login_required
def leave_event(request, event_id):
    """Authenticated users can leave the events they have previously joined"""
    if EventJoin.objects.filter(user=request.user, event_id=event_id).exists():
        EventJoin.objects.filter(user=request.user, event_id=event_id).delete()
        messages.success(request, "You have successfully left the event")
    else:
        messages.info(request, "You were not part of this event.")
    return redirect('my_events')


@login_required
def my_events(request):
    """Shows the events the user has joined"""
    participations = request.user.participations.all()
    return render(request, 'events/my_events.html', {
        'participations': participations})