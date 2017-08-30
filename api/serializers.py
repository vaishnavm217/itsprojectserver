from api.models import Houses, Members, Photos, Videos, Farms, Crops, Wells, WellWater
from rest_framework import serializers

class HousesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
        	model = Houses
        	fields = ('HID', 'Long', 'Lat', 'Income')


class MembersSerializer(serializers.HyperlinkedModelSerializer):
    	class Meta:
        	model = Members
        	fields = ('HID', 'PID', 'Age', 'Gender')

class PhotosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Photos
		fields = ('HID','PHID','URL')

class VideosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Videos
		fields = ('HID','VID','URL')

class FarmsSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Farms
                fields = ('HID', 'FID', 'Long', 'Lat')

class CropsSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Crops
                fields = ('FID', 'Year', 'Seasons')

class WellsSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Wells
                fields = ('HID', 'WID','Long', 'Lat', 'AvgYield' )

class WellWaterSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = WellWater
                fields = ('WID', 'Year', 'measured_date')
