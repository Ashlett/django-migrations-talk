from django.db import models


class Room(models.Model):

    floor = models.SmallIntegerField()
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()


class RoomReservation(models.Model):

    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()


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
    room_reservation = models.OneToOneField(RoomReservation, null=True, blank=True)
