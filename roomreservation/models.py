from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=128)
    capacity = models.IntegerField(default=0)
    is_projector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    date = models.DateField(default=datetime.now)
    comment = models.TextField(blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} {self.date}"

    # add constrains to allow for only one reservation for one day on specific room
    class Meta:
        unique_together = ('date', 'room')


