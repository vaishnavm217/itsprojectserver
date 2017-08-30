from django.db import models
import datetime

class Houses(models.Model):
	HID=models.AutoField(primary_key=True)
	Long=models.DecimalField(max_digits=6,decimal_places=6)
	Lat=models.DecimalField(max_digits=6,decimal_places=6)
	Income=models.IntegerField(default=0)

class Members(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	PID=models.AutoField(primary_key=True)
	Age=models.IntegerField(default=0)
	genders=('M','F','B','G','L','T')
	Gender=models.CharField(max_length=1,choices=genders)

class Photos(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	PHID=models.AutoField(primary_key=True)
	URL=models.CharField(max_length=200)

class Videos(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	VID=models.AutoField(primary_key=True)
	URL=models.CharField(max_length=200)

class Farms(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	FID=models.AutoField(primary_key=True)
	Long=models.DecimalField(max_digits=6,decimal_places=6)
	Lat=models.DecimalField(max_digits=6,decimal_places=6)

class Crops(models.Model):
	FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
	Year=models.IntegerField()
	seasons=["Summer","Winter","Monsoon"]
	Seasons=models.CharField(max_length=20,choices=seasons)

class Wells(models.Model):
	HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
	WID=models.AutoField(primary_key=True)
	Long=models.DecimalField(max_digits=6,decimal_places=6)
	Lat=models.DecimalField(max_digits=6,decimal_places=6)
	AvgYield=models.DecimalField(max_digits=6,decimal_places=6)

class WellWater(models.Model):
	WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
	Year=models.IntegerField()
	measured_date=models.DateField(_("Date"), default=datetime.date.today)
