# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 14:06
from __future__ import unicode_literals

from django.db import migrations


def populate_event_in_room_reservation(apps, schema_editor):
    RoomReservation = apps.get_model('roombook', 'RoomReservation')
    for reservation in RoomReservation.objects.all():
        if hasattr(reservation, 'temp'):
            reservation.event = reservation.temp
            reservation.save()


def populate_room_reservation_in_event(apps, schema_editor):
    Event = apps.get_model('roombook', 'Event')
    for event in Event.objects.all():
        if hasattr(event, 'roomreservation'):
            event.room_reservation = event.roomreservation
            event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0002_auto_20171017_1551'),
    ]

    operations = [
        migrations.RunPython(
            populate_event_in_room_reservation,
            populate_room_reservation_in_event,
        )
    ]
