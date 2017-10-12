from api.models import *
from rest_framework import serializers
'''
	Serializers
Every model/tables has its own serializer.
Serializer parses data in each table.
'''
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
        fields = ('Type','ID','PHID','photo')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('Type','ID','VID','video')

class AudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audios
        fields = ('Type','ID','AID','audio')

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
        fields = ('FID', 'WID','point', 'Depth','AvgYield' )

class YieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yields
        fields = ('WID', 'Yield', 'measured_date')
