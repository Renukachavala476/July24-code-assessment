from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from manufacturer.models import Seller
from manufacturer.serializers import SellerSerializer
from django.contrib.auth import logout


# Create your views here.

@csrf_exempt
def login_check1(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getname=Seller.objects.filter(username=username,password=password)
    seller_serializer=SellerSerializer(getname,many=True)
    if(seller_serializer.data):
        for i in seller_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminview1.html',{"data":seller_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
      


 


def loginviewadmin1(request):
    return render(request,'adminlogin1.html')

def logout_admin(request):
        logout(request)
        
        template='adminlogin1.html'
        return render(request,template)   


def myViewAllPage2(request):
    fetchdata=requests.get("http://127.0.0.1:8000/sellerapp/viewall2/").json()
    return render(request,'viewall2.html',{"data":fetchdata})



@csrf_exempt
def mySellerList2(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)




def myUpdate2(request):
    return render(request,'update2.html')



@csrf_exempt
def UpdateRead2(request):
    getNewId=request.POST.get("newid")
    getNewname=request.POST.get("newname")
    # getNewaddress=request.POST.get("newaddress")
    # getNewshopname=request.POST.get("newshopname")
    # getNewmobilenumber=request.POST.get("newmobilenumber")
    # getNewusername=request.POST.get("newusername")
    getNewpassword=request.POST.get("newpassword")
    # mydata={'name':getNewname,'address':getNewaddress,'shopname':getNewshopname,'mobilenumber':getNewmobilenumber,'username':getNewusername,'password':getNewpassword}
    mydata={'name':'getNewname','password':'getNewpassword'}
    print(mydata)
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/sellerapp/viewseller2/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Password Changed Successfully!!!")
    

@csrf_exempt
def UpdateSearchAPI2(request):
    try:
        getName=request.POST.get("name")
        getAddress=Seller.objects.filter(name=getName)
        seller_serializer=SellerSerializer(getAddress,many=True)
        return render(request,"update2.html",{"data":seller_serializer.data})
        #return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def mySellerDetails2(request,id):
    sellers=Seller.objects.get(id=id)
    if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            seller_serialize=SellerSerializer(sellers,data=dict)
            if(seller_serialize.is_valid()):
                seller_serialize.save()
                return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
