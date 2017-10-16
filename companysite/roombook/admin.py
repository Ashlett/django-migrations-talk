from django.contrib import admin

from .models import Event, Room, RoomReservation


for model in (Event, Room, RoomReservation):
    admin.site.register(model)
