from requests.sessions import Request
import json
from django.shortcuts import redirect, render
from manufacturer.models import Admin,Seller
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from manufacturer.serializers import AdminSerializer,SellerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from django.contrib.auth import logout



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
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":admin_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
      


 


def loginviewadmin(request):
    return render(request,'adminlogin.html')

def logout_admin(request):
        logout(request)
        
        template='adminlogin.html'
        return render(request,template)     



@csrf_exempt
def mySellerPage(request):
    if(request.method=="POST"):
        # dict=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=request.POST)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            #return redirect(myViewAllPage1)
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)







def mySeller(request):
    return render(request,'seller.html')

def myWelcomePage(request):
    return render(request,'welcome1.html')


def myViewAllPage1(request):
    fetchdata=requests.get("http://127.0.0.1:8000/manufacturer/viewall1/").json()
    return render(request,'viewall1.html',{"data":fetchdata})

@csrf_exempt
def mySellerDetails(request,id):
    try:
        sellers=Seller.objects.get(id=id)
        if (request.method=="GET"):    
            seller_serializer=SellerSerializer(sellers)
            return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):  
            sellers.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):  
            dict=JSONParser().parse(request)
            seller_serialize=SellerSerializer(sellers,data=dict)
            if(seller_serialize.is_valid()):
                seller_serialize.save()
                return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(seller_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


def mySearch1(request):
    return render(request,'search1.html')

def myUpdate1(request):
    return render(request,'update1.html')


def myDelete1(request):
    return render(request,'delete1.html')


@csrf_exempt
def UpdateRead1(request):
    getNewId=request.POST.get("newid")
    getNewname=request.POST.get("newname")
    getNewaddress=request.POST.get("newaddress")
    getNewshopname=request.POST.get("newshopname")
    getNewmobilenumber=request.POST.get("newmobilenumber")
    getNewusername=request.POST.get("newusername")
    getNewpassword=request.POST.get("newpassword")
    mydata={'name':getNewname,'address':getNewaddress,'shopname':getNewshopname,'mobilenumber':getNewmobilenumber,'username':getNewusername,'password':getNewpassword}
    print(mydata)
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/manufacturer/viewseller1/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPage1)
    

@csrf_exempt
def UpdateSearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Seller.objects.filter(name=getName)
        seller_serializer=SellerSerializer(getAddress,many=True)
        return render(request,"update1.html",{"data":seller_serializer.data})
        #return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


# Create your views here.
@csrf_exempt
def DeleteRead1(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/manufacturer/viewseller1/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPage1)

@csrf_exempt
def DeleteSearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Seller.objects.filter(name=getName)
        seller_serializer=SellerSerializer(getAddress,many=True)
        return render(request,"delete1.html",{"data":seller_serializer.data})
        #return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def SearchAPI1(request):
    try:
        getName=request.POST.get("name")
        getAddress=Seller.objects.filter(name=getName)
        seller_serializer=SellerSerializer(getAddress,many=True)
        return render(request,"search1.html",{"data":seller_serializer.data})
        #return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


@csrf_exempt
def mySellerList(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serializer=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
