from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    organizer = models.ForeignKey("Gamer", on_delete=CASCADE, related_name="events", related_query_name="event")
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False, default=now)
    time = models.TimeField(auto_now=False, auto_now_add=False, default=now)

    participants = models.ManyToManyField(
        "Gamer",
        related_name="participant_events",
        related_query_name="participant_event"
    )