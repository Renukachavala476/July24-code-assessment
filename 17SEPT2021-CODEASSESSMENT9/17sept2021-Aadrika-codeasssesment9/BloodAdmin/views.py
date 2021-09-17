from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from BloodAdmin.models import Donor,BloodAdmin
from BloodAdmin.serializers import BloodAdminSerializer, DonorSerializer


@csrf_exempt
def addAdmin(request):
    if (request.method=="POST"):
        
        mydata=JSONParser().parse(request)
        admin_serialize=BloodAdminSerializer(data=mydata)
        
        if (admin_serialize.is_valid()):
            admin_serialize.save()
            
            return JsonResponse(admin_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=BloodAdmin.objects.filter(username=username,password=password)
    admin_serializer=BloodAdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["username"]
            y=i["id"]
            print(x)
        request.session['username']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":admin_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
        #return render(request,'invalidpage.html')


 


def loginviewadmin(request):
    return render(request,"adminlogin.html")

def logout_admin(request):
        logout(request)
        
        template='adminlogin.html'
        return render(request,template)


@csrf_exempt
def AddDonor(request):
    if (request.method == "POST"):

        try:
            getname = request.POST.get("name")
            getaddress = request.POST.get("address")
            getbloodg = request.POST.get("bloodg")
            getmobile = request.POST.get("mobile")
            getusername = request.POST.get("username")
            getpassword = request.POST.get("password")
            getdonor = Donor.objects.filter(username=getusername)
            donor_serialiser = DonorSerializer(getdonor, many=True)
            print(donor_serialiser.data)
            if (donor_serialiser.data):
                
                return HttpResponse("donor Already Exists")


            else:
                donor_serialize = DonorSerializer(data=request.POST)
                if (donor_serialize.is_valid()):
                    donor_serialize.save()  #Save to Db
                    #return redirect(loginview)
                    return redirect(viewall)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
        except Donor.DoesNotExist:
            return HttpResponse("Invalid username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/badminss/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

@csrf_exempt
def Viewdonorall(request):
    if(request.method=="GET"):
        donor=Donor.objects.all()
        donor_serializer=DonorSerializer(donor,many=True)
        return JsonResponse(donor_serializer.data,safe=False)



def search_donor(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Donor.objects.filter(username=getnumber)
        donor_serialize=DonorSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":donor_serialize.data})
    except:   
        return HttpResponse("Invalid Username",status=status.HTTP_404_NOT_FOUND)





def update(request):
    return render(request,'updatee.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Donor.objects.filter(username=getnumber)
        donor_serialize=DonorSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":donor_serialize.data}) 
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")

        getname = request.POST.get("newname")
        getaddress = request.POST.get("newaddress")
        getbloodg = request.POST.get("newbloodg")
        getmobile = request.POST.get("newmobile")
        getusername = request.POST.get("newusername")
        getpassword = request.POST.get("newpassword")
       
        
        mydata={'name':getname,'address':getaddress,'bloodg':getbloodg,'mobile':getmobile,'username':getusername,'password':getpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/badminss/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(viewall) 
        #return HttpResponse("data has be updated successfully")


def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/badminss/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Donor.objects.filter(username=getnumber)
        donor_serialize=DonorSerializer(getnumbers,many=True)
        return render(request,"delete.html",{"data":donor_serialize.data})
    except:   
        return HttpResponse("Invalid Username")



@csrf_exempt
def Viewdonor(request,id):
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
            c_serial=DonorSerializer(d1,data=mydata)
            if(c_serial.is_valid()):
                c_serial.save()
                return JsonResponse(c_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(c_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Donor.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)

