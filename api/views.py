from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Houses, Members, Photos, Videos, Farms, Crops, Wells, Yields, Audios
from .serializers import HousesSerializer, MembersSerializer, PhotosSerializer, VideosSerializer, FarmsSerializer, CropsSerializer, WellsSerializer, YieldsSerializer,AudiosSerializer


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Houses.objects.filter(HID=request.POST["HID"])
        serializer = HousesSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        y=serializer.data
        return JsonResponse(y, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list2(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Members.objects.filter(PID=request.POST['HID'])
        serializer = MembersSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)



@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list3(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Photos.objects.filter(PHID=request.POST['HID'])
        serializer = PhotosSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)



@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list4(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Videos.objects.filter(VID=request.POST['HID'])
        serializer = VideosSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)



@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list5(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Farms.objects.filter(FID=request.POST['HID'])
        serializer = FarmsSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list6(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Crops.objects.filter(FID=request.POST['HID'])
        serializer = CropsSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)



@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list7(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Wells.objects.all()
        serializer = WellsSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def snippet_list8(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Yields.objects.filter(WID=request.POST['HID'])
        serializer = YieldsSerializer(data,many=True)
#        if serializer.is_valid():
#            serializer.save()
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def Housew(request,dat_id):
    data = {}
    house = Houses.objects.filter(HID=dat_id)
    house = HousesSerializer(house,many=True)
    data["Houses"]=house.data
    members = MembersSerializer(Members.objects.filter(HID=dat_id),many=True)
    data["Members"]=members.data
    photos = PhotosSerializer(Photos.objects.filter(HID=dat_id),many=True)
    data["Photos"]=photos.data
    videos = VideosSerializer(Photos.objects.filter(HID=dat_id),many=True)
    data["Videos"]=videos.data
    audios = AudiosSerializer(Photos.objects.filter(HID=dat_id),many=True)
    data["Audios"]=audios.data
    wells = WellsSerializer(Wells.objects.filter(HID=dat_id),many=True)
    temp = wells.data
    for i in range(len(temp)):
        k = temp[i]["WID"]
        ser = YieldsSerializer(Yields.objects.filter(WID=k),many=True)
        temp[i]["Yields"] = ser.data
    data["Wells"] = temp
    temp = FarmsSerializer(Farms.objects.filter(HID=dat_id),many=True)
    temp = temp.data
    for i in range(len(temp)):
        k = temp[i]["FID"]
        ser = CropsSerializer(Crops.objects.filter(FID=k),many=True)
        temp[i]["Crops"] = ser.data
    data["Farms"] = temp
    return JsonResponse(data, status=201,safe=False)
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def HouseALL(request):
    data={}
    house=Houses.objects.all()
    house=HousesSerializer(house,many=True)
    temp=house.data
    for i in range(len(temp)):
        data[i]={}
        home=HousesSerializer(Houses.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Houses"]=home.data
        members=MembersSerializer(Members.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Members"]=members.data
        photos=PhotosSerializer(Photos.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Photos"]=photos.data
        videos=VideosSerializer(Videos.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Videos"]=videos.data
        audios=AudiosSerializer(Audios.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Audios"]=audios.data
        wells = WellsSerializer(Wells.objects.filter(HID=temp[i]["HID"]),many=True)
        temp2 = wells.data
        for j in range(len(temp2)):
            k = temp2[j]["WID"]
            ser = YieldsSerializer(Yields.objects.filter(WID=k),many=True)
            temp2[j]["Yields"] = ser.data
        data[i]["Wells"] = temp2
        farms = FarmsSerializer(Farms.objects.filter(HID=temp[i]["HID"]),many=True)
        temp2 = farms.data
        for j in range(len(temp2)):
            k = temp2[j]["FID"]
            ser = CropsSerializer(Crops.objects.filter(FID=k),many=True)
            temp2[j]["Crops"] = ser.data
        data[i]["Farms"] = temp2
    return JsonResponse(data, status=201,safe=False)
