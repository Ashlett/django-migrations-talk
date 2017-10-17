# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 15:56
from __future__ import unicode_literals

from django.db import migrations


def swap_training_and_interview(apps, schema_editor):
    Event = apps.get_model('roombook', 'Event')
    training_ids = Event.objects.filter(category='training').values_list('id', flat=True)
    interview_ids = Event.objects.filter(category='interview').values_list('id', flat=True)
    Event.objects.filter(id__in=training_ids).update(category='interview')
    Event.objects.filter(id__in=interview_ids).update(category='training')


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0004_remove_event_room_reservation'),
    ]

    operations = [
        migrations.RunPython(swap_training_and_interview, swap_training_and_interview)
    ]