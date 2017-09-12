from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

class Houses(models.Model):
    HID=models.AutoField(primary_key=True)
    income=models.FloatField(default=0.0)
    point=models.PointField(default=Point(1,1),null=True)
    def __str__(self):
        return "%s" %(self.HID)

class Members(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    PID=models.AutoField(primary_key=True)
    Age=models.IntegerField(default=0)
    genders=(('M',"Male"),('F',"Female"))
    Name=models.CharField(max_length=30,default="")
    Gender=models.CharField(max_length=1,choices=genders)
    def __str__(self):
        return "%s : %s" %(self.PID,self.Name)


class Photos(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    PHID=models.AutoField(primary_key=True)
    photo=models.FileField(upload_to = 'uploaded_images/')
    def __str__(self):
        return "%s : %s" % (self.HID,self.PHID)

class Videos(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    VID=models.AutoField(primary_key=True)
    URL=models.CharField(max_length=200)
    def __str__(self):
        return "%s : %s" % (self.HID,self.VID)

class Farms(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    FID=models.AutoField(primary_key=True)
    plot=models.PolygonField(srid=4326,geography=True)
    def __str__(self):
        return "%s" % (self.FID)

class Crops(models.Model):
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    Year=models.IntegerField()
    seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    Seasons=models.CharField(max_length=20,choices=seasons)
    def __str__(self):
        return "%s : %s" %(self.FID,self.Year)

class Wells(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    WID=models.AutoField(primary_key=True)
    point=models.PointField(default=Point(1,1))
    AvgYield=models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return "%s" %(self.WID)

class WellWater(models.Model):
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
    Year=models.IntegerField()
    Yield=models.FloatField(default=0.0)
    measured_date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return "%s : %s" %(self.WID,self.WID)
