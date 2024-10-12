from django.contrib import admin

from .models import Saccos, Drivers, Destinations, Conductors, Routes

# Register your models here.
admin.site.register(Saccos)
admin.site.register(Drivers)
admin.site.register(Destinations)
admin.site.register(Conductors)
admin.site.register(Routes)
