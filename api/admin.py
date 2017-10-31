from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class PInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
class ImageAdmin(admin.GeoModelAdmin):
	# ImageAdmin:
	# Custom admin interface for viewing and validation of images.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
	fields = ( 'Type','HID','FID','WID','image_tag','photo' )
	readonly_fields = ('image_tag',)

class VideoAdmin(admin.GeoModelAdmin):
	# VideoAdmin:
	# Custom admin interface for viewing and validation of Videos.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
	fields = ( 'Type','HID','FID','WID','image_tag','video' )
	readonly_fields = ('image_tag',)

class AudioAdmin(admin.GeoModelAdmin):
	# ImageAdmin:
	# Custom admin interface for viewing and validation of Audio.
	# Parameter Displayed:
	# 	Type, HID, FID, WID, image_tag, photo
	# Read Only Parameters:
	# 	image_tag
	fields = ( 'Type','HID','FID','WID','image_tag','audio' )
	readonly_fields = ('image_tag',)

admin.site.register(UserProfile)
admin.site.register(Houses,admin.GeoModelAdmin)
admin.site.register(Members,admin.GeoModelAdmin)
admin.site.register(Farms,admin.GeoModelAdmin)
admin.site.register(Photos,ImageAdmin)
admin.site.register(Videos,VideoAdmin)
admin.site.register(Audios,AudioAdmin)
admin.site.register(Crops,admin.GeoModelAdmin)
admin.site.register(Wells,admin.GeoModelAdmin)
admin.site.register(Yields,admin.GeoModelAdmin)
