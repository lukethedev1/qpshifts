from django.contrib import admin
from shifts.models import Location, Record, UserLocation


admin.site.register(Location)
admin.site.register(Record)
admin.site.register(UserLocation)
