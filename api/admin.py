from django.contrib.gis import admin
from .models import *
class ImageAdmin(admin.OSMGeoAdmin):
	# ImageAdmin:
	# Custom admin interface for viewing and validation of images.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
	fields = ( 'Type','HID','FID','WID','image_tag','photo' )
	readonly_fields = ('image_tag',)

class VideoAdmin(admin.OSMGeoAdmin):
	# VideoAdmin:
	# Custom admin interface for viewing and validation of Videos.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
	fields = ( 'Type','HID','FID','WID','image_tag','video' )
	readonly_fields = ('image_tag',)

class AudioAdmin(admin.OSMGeoAdmin):
	# ImageAdmin:
	# Custom admin interface for viewing and validation of Audio.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
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
