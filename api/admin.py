from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Houses,admin.GeoModelAdmin)
admin.site.register(Members,admin.GeoModelAdmin)
admin.site.register(Farms,admin.GeoModelAdmin)
admin.site.register(Photos,admin.GeoModelAdmin)
admin.site.register(Videos,admin.GeoModelAdmin)
admin.site.register(Crops,admin.GeoModelAdmin)
admin.site.register(Wells,admin.GeoModelAdmin)
admin.site.register(WellWater,admin.GeoModelAdmin)