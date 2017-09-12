from api.models import Houses, Members, Photos, Videos, Farms, Crops, Wells, WellWater
from rest_framework import serializers
class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ('HID', 'point','income')


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('HID','Name', 'PID', 'Age', 'Gender')

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('HID','PHID','URL')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('HID','VID','URL')

class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = ('HID', 'FID', 'plot')

class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ('FID', 'Year', 'Seasons')

class WellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wells
        fields = ('HID', 'WID','point', 'AvgYield' )

class WellWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellWater
        fields = ('WID', 'Year', 'measured_date')
