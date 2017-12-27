from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from . import models

admin.site.register(models.Shop)
admin.site.register(models.Verein)
admin.site.register(models.Event)
admin.site.register(models.Buddy)
