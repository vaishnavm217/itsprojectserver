from django.contrib.gis import admin
from .models import *

# Register your models here.
class ImageAdmin(admin.OSMGeoAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'Type','HID','FID','WID','image_tag','photo' )
    readonly_fields = ('image_tag',)
class VideoAdmin(admin.OSMGeoAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'Type','HID','FID','WID','image_tag','video' )
    readonly_fields = ('image_tag',)
class AudioAdmin(admin.OSMGeoAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'Type','HID','FID','WID','image_tag','audio' )
    readonly_fields = ('image_tag',)
admin.site.register(Houses,admin.OSMGeoAdmin)
admin.site.register(Members,admin.OSMGeoAdmin)
admin.site.register(Farms,admin.OSMGeoAdmin)
admin.site.register(Photos,ImageAdmin)
admin.site.register(Videos,VideoAdmin)
admin.site.register(Audios,AudioAdmin)
admin.site.register(Crops,admin.OSMGeoAdmin)
admin.site.register(Wells,admin.OSMGeoAdmin)
admin.site.register(Yields,admin.OSMGeoAdmin)