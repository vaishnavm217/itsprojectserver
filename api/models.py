from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import mark_safe

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

class Farms(models.Model):
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
    Name=models.CharField(max_length=50,default="Rice")
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    Year=models.IntegerField()
    seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    Seasons=models.CharField(max_length=20,choices=seasons)
    Area=models.FloatField(default=0.0)
    def __str__(self):
        return "%s : %s" %(self.FID,self.Year)

class Wells(models.Model):
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    WID=models.AutoField(primary_key=True)
    point=models.PointField(default=Point(1,1))
    AvgYield=models.FloatField(default=0.0)
    Depth=models.FloatField(default=0.0)
    def __str__(self):
        return "%s" %(self.WID)

class Yields(models.Model):
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
    types=(('WID','Well'),('FID','Farm',),('HID','House'))
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    PHID=models.AutoField(primary_key=True)
    photo=models.ImageField(upload_to = 'uploaded_images/')
    def __str__(self):
        return "%s-%s : %s" % (self.Type,self.ID,self.PHID)
    def image_tag(self):
        return mark_safe("<img src='%s'>" % (self.photo))  
    image_tag.short_description = 'photo'
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID

class Videos(models.Model):
    types=(('WID','Well'),('FID','Farm',),('HID','House'))
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    VID=models.AutoField(primary_key=True)
    video=models.FileField(upload_to = 'uploaded_video/')
    def __str__(self):
        return "%s-%s : %s" % (self.Type,self.ID,self.VID)
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID

class Audios(models.Model):
    types=(('WID','Well'),('FID','Farm',),('HID','House'))       
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    AID=models.AutoField(primary_key=True)
    audio=models.FileField(upload_to = 'uploaded_audio/')
    def __str__(self):
        return "%s-%s : %s" % (self.Type,self.ID,self.AID)
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID
