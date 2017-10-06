from api.models import *
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
        fields = ('HID','PHID','file')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('HID','VID','file')

class AudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = ('HID','AID','file')

class FarmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = ('HID', 'FID', 'plot','area')

class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ('Name','FID', 'Year', 'Seasons','Area')

class WellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wells
        fields = ('HID', 'WID','point', 'AvgYield' )

class YieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yields
        fields = ('WID', 'Yield', 'measured_date')
