from django.db import models
from datetime import time

class Room(models.Model):
    room_name = models.CharField(max_length= 100)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.room_name} on floor {self.floor_number} at room #: {self.room_number}"

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
