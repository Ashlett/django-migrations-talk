from django.db import models


class Room(models.Model):

    floor = models.SmallIntegerField()
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return 'Room {} {}'.format(self.symbol, self.name)


class RoomReservation(models.Model):

    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{}: {}'.format(self.room, self.start)


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

    def __str__(self):
        return '{}: {}'.format(self.title, self.start)
