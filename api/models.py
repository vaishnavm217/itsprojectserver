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
super().save(self)
    	temp = Yields.objects.filter(WID=self.WID)
    	avg = sum([i.Yield for i in temp])/len(temp)
    	wellt = Wells.object.filter(WID=self.WID)
    	wellt.AvgYield=avg
    	wellt.save()

class Crops(models.Model):
    Name=models.CharField(max_length=50,default="Rice")
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    Year=models.IntegerField()
    seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    Seasons=models.CharField(max_length=20,choices=seasons)
    Area=models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return "%s : %s" %(self.FID,self.Year)

class Wells(models.Model):
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    WID=models.AutoField(primary_key=True)
    point=models.PointField(default=Point(1,1))
    AvgYield=models.DecimalField(max_digits=7,decimal_places=4,default=0)
    Depth=models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return "%s" %(self.WID)

class Yields(models.Model):
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
    Yield=models.FloatField(default=0.0)
    measured_date=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return "%s : %s" %(self.WID,self.measured_date)
    def save(self):
    	super().save(self)
    	temp = Yields.objects.filter(WID=self.WID)
    	avg = sum([i.Yield for i in temp])/len(temp)
    	wellt = Wells.object.filter(WID=self.WID)
    	wellt.AvgYield=avg
    	wellt.save()

class Photos(models.Model):
    types=(('WID','WID'),('FID','FID'),('HID','HID'))
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    PHID=models.AutoField(primary_key=True)
    file=models.ImageField(upload_to = 'uploaded_images/')
    def __str__(self):
        return "%s : %s" % (self.HID,self.PHID)
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID

class Videos(models.Model):
    types=(('WID','WID'),('FID','FID'),('HID','HID'))
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    VID=models.AutoField(primary_key=True)
    file=models.FileField(upload_to = 'uploaded_video/')
    def __str__(self):
        return "%s : %s" % (self.HID,self.VID)
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID

class Audios(models.Model):
    types=(('WID','WID'),('FID','FID'),('HID','HID'))
    Type=models.CharField(max_length=3,choices=types)
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE,blank=True)
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE,blank=True)
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE,blank=True)
    AID=models.AutoField(primary_key=True)
    file=models.FileField(upload_to = 'uploaded_audio/')
    def __str__(self):
        return "%s : %s" % (self.HID,self.AID)
    @property
    def ID(self):
        if self.Type=="WID":
            return self.WID
        elif self.Type=="HID":
            return self.HID
        else:
            return self.FID
