from django.contrib import admin

from events.models import Event, Sensor

admin.site.register(Event)
admin.site.register(Sensor)
