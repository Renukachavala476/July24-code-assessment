from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from manufacturer.models import Manufacturer,Seller
from manufacturer.serializers import ManufacturerSerializer,SellerSerializer

@csrf_exempt
def loginCheck(request):
    try:

        getsusername=request.POST.get("username")
        getspassword=request.POST.get("password")
        getPatient=Seller.objects.filter(username=getsusername,password=getspassword)
        pserialize=SellerSerializer(getPatient,many=True)

        if(pserialize.data):
            for i in pserialize.data:
                getid=i["id"]
                getpname=i['name']
                getpaddress=i['address']
                


            request.session['uid']=getid
            request.session['uname']=getpname
            data={"name":getpname,"paddress":getpaddress}
            return render(request,"welcome.html",{"data":data})

        else:
            return HttpResponse("Invalid Credentials")

    except Seller.DoesNotExist:
        return HttpResponse("Invalid Empoyee Code")
    # except:
    #     return HttpResponse("Something went wrong")

def loginview(request):
    return render(request,'login.html')



@csrf_exempt
def ViewCustomer(request,id):
    try:
        c1=Seller.objects.get(id=id)
        if(request.method=="GET"):
            customer_serializer=SellerSerializer(c1)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            c_serial=SellerSerializer(c1,data=mydata)
            if(c_serial.is_valid()):
                c_serial.save()
                return JsonResponse(c_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(c_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Seller.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)



def update(request):
    return render(request,'update.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Seller.objects.filter(username=getnumber)
        customer_serialize=SellerSerializer(getnumbers,many=True)
        return render(request,"update.html",{"data":customer_serialize.data})
    except Seller.DoesNotExist:   
        return HttpResponse("Invalid username",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")
        getnewpassword=request.POST.get("newpassword")
        
        
        mydata={'password':getnewpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/seller/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("Password changed succesfully")



