from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bloodbank.serializers import DonorSerializer
import json
from bloodbank.models import Donor
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def searchapi(request):
    try:
        getdonorcode=request.POST.get("donorcode")
        getdonor=Donor.objects.filter(donorcode=getdonorcode)
        donor_serializer=DonorSerializer(getdonor,many=True)
        return render(request,"search.html",{"data":donor_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def donor_details(request,fetchid):
    try:
        donors=Donor.objects.get(id=fetchid)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid donor id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        donor_serializer=DonorSerializer(donors)
        return JsonResponse(donor_serializer.data,safe=False)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        donor_serialize=DonorSerializer(donors,data=mydict)
        if (donor_serialize.is_valid()):
            donor_serialize.save()
    if(request.method=="DELETE"):
        donors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)




@csrf_exempt
def donor_list(request):
    if (request.method=="GET"):
        donors=Donor.objects.all()
        donor_serializer=DonorSerializer(employees,many=True)
        return JsonResponse(donor_serializer.data,safe=False)



@csrf_exempt
def donoraddpage(request):
    if(request.method =="POST"):
        # getname=request.POST.get("name")
        # getcode=request.POST.get("donorcode")
        # getaddress=request.POST.get("address")
        # getmobilenumber=request.POST.get("mobilenumber")
        # getbloodgroup=request.POST.get("bloodgroup")
        # getusername=request.POST.get("username")
        # getpassword=request.POST.get("password")
        # mydict={"name":getname,"donorcode":getcode,"address":getaddress,"mobilenumber":getmobilenumber,"bloodgroup":getbloodgroup,"username":getusername,"password":getpassword}
        donor_serialize=DonorSerializer(data=request.POST)
        if (donor_serialize.is_valid()):
            donor_serialize.save()
            #return HttpResponse("success")
            return redirect(don_view)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
            
        # return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
def donor_view(request):
    return render(request,'index1.html')
def don_view(request):
    fetchdata=requests.get('http://localhost:8000/donor/viewdonor/').json()
    return render(request,'viewall.html',{"data":fetchdata})
    #return render(request,'viewall.html')
def upd_view(request):
    return render(request,'update.html')
def del_view(request):
    return render(request,'delete.html')
def search_view(request):
    return render(request,'search.html')
@csrf_exempt
def updatesearchapi(request):
    try:
        getcode=request.POST.get("donorcode")
        getdonor=Donor.objects.filter(donorcode=getcode)
        donor_serializer=DonorSerializer(getdonor,many=True)
        return render(request,"update.html",{"data":donor_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def update_data_read(request):
    getname=request.POST.get("newname")
    getid=request.POST.get("newid")
    getaddress=request.POST.get("newaddress")
    getcode=request.POST.get("newdonorcode")
    getmobilenumber=request.POST.get("newmobilenumber")
    getbloodgroup=request.POST.get("newbloodgroup")
    getusername=request.POST.get("newusername")
    getpassword=request.POST.get("newpassword")
    mydata={'name':getname,'donorcode':getcode,'address':getaddress,'mobilenumber':getmobilenumber,'bloodgroup':getbloodgroup,'username':getusername,'password':getpassword}
    jsondata=json.dumps(mydata)
    Apilink="http://localhost:8000/donor/viewdonor/" + getid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def delete_data_read(request):

    getnewid=request.POST.get("newid")
    Apilink="http://localhost:8000/donor/viewdonor/" + getnewid
    requests.delete(Apilink)
    return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getcode=request.POST.get("donorcode")
        getdonor=Donor.objects.filter(donorcode=getcode)
        donor_serializer=DonorSerializer(getdonor,many=True)
        return render(request,"delete.html",{"data":donor_serializer.data})
        #return JsonResponse(employee_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Donor.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")



