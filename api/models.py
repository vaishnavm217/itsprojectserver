from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import os
'''
Validation functions
'''
def validate_video_extension(value):
	ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
	valid_extensions = ['.avi', '.mov', '.flv', '.mpeg', '.mp4', '.wmv', '.mkv','.gif']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'Unsupported file extension.')
def validate_audio_extension(value):
	ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
	valid_extensions = ['.wav', '.mp3', '.aac', '.wma', '.flac']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'Unsupported file extension.')
'''
	Database
Major tables:
1.Houses
2.Members
3.Farms
4.Crops
5.Wells
6.Yields
7.Photos
8.Videos
9.Audios
'''

class UserProfile(models.Model):
   user = models.OneToOneField(User)
   Phone = models.CharField(max_length=256, blank=True, null=True)
   HID=models.ForeignKey('Houses',to_field='HID',on_delete=models.CASCADE)
   PID=models.ForeignKey('Members',to_field='PID',on_delete=models.CASCADE)

class Houses(models.Model):
	'''
			Houses
	HID-(House ID)Primary key
	income-income of each house
	point-GIS coordinates of each house
	'''
	HID=models.AutoField(primary_key=True)
	income=models.FloatField(default=0.0)
	point=models.PointField(default=Point(1,1),null=True)
	def __str__(self):
		return "%s" %(self.HID)

class Members(models.Model):
	'''
			Members
	HID-Foreign key ref to Houses
	PID-Person ID primary key
	Age-Age of the members
	Gender-Gender of person
	Name-Person name
	'''
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	PID=models.AutoField(primary_key=True)
	Age=models.IntegerField(default=0)
	genders=(('M',"Male"),('F',"Female"))
	Name=models.CharField(max_length=30,default="")
	Gender=models.CharField(max_length=1,choices=genders)
	def __str__(self):
		return "%s : %s" %(self.PID,self.Name)

class Farms(models.Model):
	'''
			Farms
	HID-Foreign key ref to Houses
	FID-Farm ID Primary key
	plot-GIS polygon of farm
	area-Area of farm
	'''
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	FID=models.AutoField(primary_key=True)
	plot=models.PolygonField(srid=4326,geography=True)
	area=models.FloatField(default=0.0)
	def __str__(self):
		return "%s" % (self.FID)
	def save(self):
		temp=self.plot.transform(27700,clone=True)
		self.area=temp.area
		super().save(self)
class Crops(models.Model):
	'''
			Crops
	Name-Crop name
	FID-Foreign key ref to Farms
	Year-Year in which the crop was grown
	Seasons-Season of cultivation
	Area-Area of farm in which the crop was grown
	'''
	Name=models.CharField(max_length=50,default="Rice")
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	Year=models.IntegerField()
	seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
	Seasons=models.CharField(max_length=20,choices=seasons)
	Area=models.FloatField(default=0.0)
	def __str__(self):
		return "%s : %s" %(self.FID,self.Year)

class Wells(models.Model):
	'''
			Wells
	FID-Foreign key ref to Farms
	WID-Well ID Primary key
	point-GIS coordinates of well
	AvgYield-Average of all yields(m)
	Depth-Depth of well(m)
	'''
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	WID=models.AutoField(primary_key=True)
	point=models.PointField(default=Point(1,1))
	AvgYield=models.FloatField(default=0.0)
	Depth=models.FloatField(default=0.0)
	def __str__(self):
		return "%s" %(self.WID)

class Yields(models.Model):
	'''
	Yields
	WID-Foreign key ref to wells
	Yield-Yield measured on that date(m)
	measured_date-Date on which yield was measured
	'''
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
	Yield=models.FloatField(default=0.0)
	measured_date=models.DateTimeField(default=datetime.datetime.now())
	def __str__(self):
		return "%s : %s" %(self.WID,self.measured_date)
	def clean(self):
		if(self.Yield>self.WID.Depth):
			raise ValidationError("Yield more than Depth. Depth:"+str(self.WID.Depth))


	def save(self):
		self.full_clean()
		super().save(self)
		temp = Yields.objects.filter(WID=self.WID)
		avg = sum([i.Yield for i in temp])/len(temp)
		wellt = Wells.objects.filter(WID=self.WID.WID)
		for i in wellt:
			i.AvgYield=avg
			i.save()

class Photos(models.Model):
	'''
	Photos
	Type-Specifiying type of ID
	ID-Foreign key to specify type
	PHID-Photo ID
	photo-the image
	'''
	types=(('WID','Well'),('FID','Farm',),('HID','House'))
	Type=models.CharField(max_length=3,choices=types)
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True,null=True)
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True,null=True)
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True,null=True)
	PHID=models.AutoField(primary_key=True)
	photo=models.ImageField(upload_to = 'uploaded_images/')
	@property
	def ID(self):
		if self.Type=="WID":
			return self.WID.WID
		elif self.Type=="HID":
			return self.HID.HID
		else:
			return self.FID.FID
	def __str__(self):
		return "%s-%s : %s" % (self.Type,self.ID,self.PHID)
	def image_tag(self):
		if self.photo:
			return mark_safe("<img src='/media/{}' style='width:50%'>".format(self.photo))
		else:
			return mark_safe("<p>No image Uploaded</p>")
	image_tag.short_description = 'Preview'


class Videos(models.Model):
	'''
	Videos
	Type-Specifiying type of ID
	ID-Foreign key to specify type
	VID-Video ID
	video-the video
	'''
	types=(('WID','Well'),('FID','Farm',),('HID','House'))
	Type=models.CharField(max_length=3,choices=types)
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True,null=True)
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True,null=True)
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True,null=True)
	VID=models.AutoField(primary_key=True)
	video=models.FileField(upload_to = 'uploaded_video/',validators=[validate_video_extension])
	def __str__(self):
		return "%s-%s : %s" % (self.Type,self.ID,self.VID)
	def image_tag(self):
		if self.video:
			return mark_safe("<video controls  style='width:50%'><source src='/media/{}'></video>".format(self.video))
		else:
			return mark_safe("<p>No Video Uploaded</p>")
	image_tag.short_description = 'Preview'
	@property
	def ID(self):
		if self.Type=="WID":
			return self.WID.WID
		elif self.Type=="HID":
			return self.HID.HID
		else:
			return self.FID.FID

class Audios(models.Model):
	'''
	Audios
	Type-Specifiying type of ID
	ID-Foreign key to specify type
	AID-Audio ID
	audio-the sound file
	'''
	types=(('WID','Well'),('FID','Farm',),('HID','House'))
	Type=models.CharField(max_length=3,choices=types)
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True,null=True)
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True,null=True)
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True,null=True)
	AID=models.AutoField(primary_key=True)
	audio=models.FileField(upload_to = 'uploaded_audio/',validators=[validate_audio_extension])
	def __str__(self):
		return "%s-%s : %s" % (self.Type,self.ID,self.AID)
	def image_tag(self):
		if self.audio:
			return mark_safe("<audio controls><source src='/media/{}'></audio>".format(self.audio))
		else:
			return mark_safe("<p>No image Uploaded</p>")
	image_tag.short_description = 'Preview'
	@property
	def ID(self):
		if self.Type=="WID":
			return self.WID.WID
		elif self.Type=="HID":
			return self.HID.HID
		else:
			return self.FID.FID
