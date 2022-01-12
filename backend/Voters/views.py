from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Voters.models import County,Voters
from Voters.serializers import CountySerializer,VoterSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def countyApi(request,id=0):
    if request.method=='GET':
        county = County.objects.all()
        county_serializer = CountySerializer(county, many=True)
        return JsonResponse(county_serializer.data, safe=False)

    elif request.method=='POST':
        county_data=JSONParser().parse(request)
        county_serializer = CountySerializer(data=county_data)
        if county_serializer.is_valid():
            county_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        county_data = JSONParser().parse(request)
        county=County.objects.get(DepartmentId=county_data['DepartmentId'])
        county_serializer=CountySerializer(county,data=county_data)
        if county_serializer.is_valid():
            county_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        county=County.objects.get(DepartmentId=id)
        county.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def votersApi(request,id=0):
    if request.method=='GET':
        voters = Voters.objects.all()
        voters_serializer = VoterSerializer(voters, many=True)
        return JsonResponse(voters_serializer.data, safe=False)

    elif request.method=='POST':
        voters_data=JSONParser().parse(request)
        voters_serializer = VoterSerializer(data=voters_data)
        if voters_serializer.is_valid():
            voters_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        voters_data = JSONParser().parse(request)
        voters=Voters.objects.get(VoterId=voters_data['VoterId'])
        voters_serializer=VoterSerializer(Voters,data=voters_data)
        if voters_serializer.is_valid():
            voters_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        voters=Voters.objects.get(EmployeeId=id)
        voters.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)