from django.db import models
from django.utils import timezone


class Room(models.Model):

    floor = models.SmallIntegerField()
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return 'Room {} {} ({})'.format(self.symbol, self.name, self.capacity)


class RoomReservation(models.Model):

    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()
    event = models.OneToOneField('Event', null=True, blank=True)

    def __str__(self):
        return '{}: {:%Y-%m-%d %H:%M} - {:%Y-%m-%d %H:%M}'.format(
            self.room, timezone.localtime(self.start), timezone.localtime(self.end)
        )


class Event(models.Model):

    MEETING = 'meeting'
    TRAINING = 'training'
    INTERVIEW = 'interview'

    CATEGORY_CHOICES = (
        (MEETING, 'Meeting'),
        (TRAINING, 'Training'),
        (INTERVIEW, 'Interview'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=MEETING)
    room_reservation = models.OneToOneField(
        RoomReservation, null=True, blank=True, related_name='temp'
    )

    def __str__(self):
        return '{} on {:%Y-%m-%d (%a) at %H:%M}'.format(self.title, timezone.localtime(self.start))
