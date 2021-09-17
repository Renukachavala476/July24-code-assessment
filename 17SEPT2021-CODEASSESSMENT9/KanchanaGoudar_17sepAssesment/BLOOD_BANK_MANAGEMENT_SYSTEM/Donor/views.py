from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Admin.models import Donor
from Admin.serializers import DonorSerializer
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def login_checkdonor(request):
    getusername=request.POST.get("Username")
    print(getusername)
    getpassword=request.POST.get("Password")
    print(getpassword)
    getdonor=Donor.objects.filter(Username=getusername,Password=getpassword)
    donor_s=DonorSerializer(getdonor,many=True)
    if(donor_s.data):
        for i in donor_s.data:
            x=i["Name"]
            print(x)
        request.session['uname']=x
        return render(request,'viewsdonor.html',{"data":donor_s.data})
    else:
        return HttpResponse("Invalid Credentials")
        

@csrf_exempt
def logindonor(request):
    return render(request,"login.html")


##DONOR VIEW##
@csrf_exempt
def ViewallDonor(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serializer=DonorSerializer(donor,many=True)
        return JsonResponse(donor_serializer.data,safe=False)


@csrf_exempt
def Donorviewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/Donor/viewallapi/").json()
    return render(request,'viewsdonor.html',{"data":fetchdata})

@csrf_exempt
def ViewDonor(request,id):
    try:
        d1=Donor.objects.get(id=id)
        if(request.method=="GET"):
            donor_serializer=DonorSerializer(d1)
            return JsonResponse(donor_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            d1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            d_serial=DonorSerializer(d1,data=mydata)
            if(d_serial.is_valid()):
                d_serial.save()
                return JsonResponse(d_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(d_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)
 

 ##CHANGE PASSWORD
@csrf_exempt
def changepassword(request):
    return render(request,'updatepassword.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getu=request.POST.get("newid")
        getnames=Donor.objects.filter(id=getu)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"updatepassword.html",{"data":donor_serialize.data})
    except Donor.DoesNotExist:   
        return HttpResponse("Invalid Name",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):
        getId=request.POST.get("newid")
        getname=request.POST.get("newname")    
        getaddress=request.POST.get("newaddress")
        getbgroup=request.POST.get("newbgroup")
        getmobilenumber=request.POST.get("newmobilenumber")
        getusername=request.POST.get("newusername")
        getpassword=request.POST.get("newpassword")
        mydata={'Name':getname,'Address':getaddress,'Bgroup':getbgroup,'Mobilenumber':getmobilenumber,'Username':getusername,'Password':getpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/Donor/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(Donorviewall) 

@csrf_exempt
def logoutdonor(request):
    logout(request)
    
    template='login.html'
    return render(request,template)    