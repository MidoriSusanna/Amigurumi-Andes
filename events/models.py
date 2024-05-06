from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """ Store event details """
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} at {self.location} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"

class EventJoin(models.Model):
    # Each participation is related to one user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participations")
    # Each participation is related to one event
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")

    class Meta:
        """ Ensures that each user can only participate in each event once """
        unique_together = ['user', 'event']

    def __str__(self):
        return f"{self.user.username} participating in {self.event.name}"
