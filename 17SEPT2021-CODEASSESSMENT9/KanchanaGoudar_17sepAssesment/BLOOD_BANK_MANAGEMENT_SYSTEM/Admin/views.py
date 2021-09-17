from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Admin.models import Admin,Donor
from Admin.serializers import AdminSerializer,DonorSerializer
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests


@csrf_exempt
def addadmin(request):
    if (request.method=="POST"):
        
        mydata=JSONParser().parse(request)
        admin_serialize=AdminSerializer(data=mydata)
        
        if (admin_serialize.is_valid()):
            admin_serialize.save()
            
            return JsonResponse(admin_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def login_checkadmin(request):
    getusername=request.POST.get("Username")
    getpassword=request.POST.get("Password")
    getadmin=Admin.objects.filter(Username=getusername,Password=getpassword)
    admin_s=AdminSerializer(getadmin,many=True)
    if(admin_s.data):
        for i in admin_s.data:
            x=i["Adminname"]
            print(x)
        request.session['uname']=x
        return render(request,'dashboard.html',{"data":admin_s.data})
    else:
        return HttpResponse("Invalid Credentials")
        

@csrf_exempt
def loginadminview(request):
    return render(request,"loginadmin.html")


@csrf_exempt
def logoutadmin(request):
    logout(request)
    
    template='loginadmin.html'
    return render(request,template)  

####DONOR########

@csrf_exempt
def AddDonor(request):

    if (request.method == "POST"):
        donor_serialize = DonorSerializer(data=request.POST)
       
        if (donor_serialize.is_valid()):
            donor_serialize.save()  #Save to Db
            return redirect(Donorviewall)   


        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def DonorAdd(request):
    return render(request,'Adddonor.html')

##DONOR VIEW##
@csrf_exempt
def ViewallDonor(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serializer=DonorSerializer(donor,many=True)
        return JsonResponse(donor_serializer.data,safe=False)


@csrf_exempt
def Donorviewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/Admin/viewallapi/").json()
    return render(request,'views.html',{"data":fetchdata})

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

@csrf_exempt
def search_donor(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getname=request.POST.get("Bgroup")
        getnames=Donor.objects.filter(Bgroup=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"search.html",{"data":donor_serialize.data})
    except:   
        return HttpResponse("Invalid Name",status=status.HTTP_404_NOT_FOUND)

##DONOR UPDATE##
@csrf_exempt
def update(request):
    return render(request,'update.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getb=request.POST.get("mobilenumber")
        getnames=Donor.objects.filter(Mobilenumber=getb)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"update.html",{"data":donor_serialize.data})
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
        ApiLink="http://127.0.0.1:8000/Admin/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(Donorviewall)   

##DONOR deelete
@csrf_exempt
def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/Admin/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(Donorviewall)

@csrf_exempt
def delete_search_api(request):
    # try:
        getname=request.POST.get("Name")
        getnames=Donor.objects.filter(Name=getname)
        donor_serialize=DonorSerializer(getnames,many=True)
        return render(request,"delete.html",{"data":donor_serialize.data})
    # except:   
    #     return HttpResponse("Invalid Name")    