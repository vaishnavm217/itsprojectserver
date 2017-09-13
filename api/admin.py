from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Houses,admin.OSMGeoAdmin)
admin.site.register(Members,admin.OSMGeoAdmin)
admin.site.register(Farms,admin.OSMGeoAdmin)
admin.site.register(Photos,admin.OSMGeoAdmin)
admin.site.register(Videos,admin.OSMGeoAdmin)
admin.site.register(Audios,admin.OSMGeoAdmin)
admin.site.register(Crops,admin.OSMGeoAdmin)
admin.site.register(Wells,admin.OSMGeoAdmin)
admin.site.register(Yields,admin.OSMGeoAdmin)