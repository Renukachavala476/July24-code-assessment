from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests.sessions import Request
from manufacturer.serializer import ManufacturerSerializer,SellerSerializer
from manufacturer.models import Manufacturer,Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import requests
# Create your views here.

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def selleradd(request):
    return render(request,'addseller.html')

def sellerview(request):
    fetch = requests.get("http://127.0.0.1:8000/manufacturer/sellerview/").json
    return render(request,'viewseller.html',{"data":fetch})

def s_update(request):
    return render(request,'updateseller.html')

def s_delete(request):
    return render(request,'deleteseller.html')

@csrf_exempt
def registermanufacturer(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        # manu_serializer = ManufacturerSerializer(data=mydata)
        manu_serializer = ManufacturerSerializer(data=request.POST)
        if(manu_serializer.is_valid()):
            manu_serializer.save()
            # return JsonResponse(manu_serializer.data,status=status.HTTP_200_OK)
            return redirect(login)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def regiview(request):
    if(request.method == "GET"):
        manu = Manufacturer.objects.all()
        manu_serializer = ManufacturerSerializer(manu,many=True)
        return JsonResponse(manu_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def login_check(request):
    try:
        getusername = request.POST.get("username")
        getpassword = request.POST.get("password")
        getuser = Manufacturer.objects.filter(username = getusername,password = getpassword)
        user_serializer = ManufacturerSerializer(getuser,many=True)
        print(user_serializer)
        if(user_serializer.data):
            for i in user_serializer.data:
                getid = i["id"]
                getname = i["name"]
                getusername = i["username"]
            request.session['uid'] = getid
            request.session['uname'] = getname
            data = {"name":getname,"username":getusername}
            # return HttpResponse(data)
            return render(request,'profile.html',{"data":data})
        else:
            return HttpResponse("Invalid credientials")
    except Manufacturer.DoesNotExist:
        return HttpResponse("Invalid username")
    except:
        return HttpResponse("Something went wrong")


@csrf_exempt
def seller_add(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        # seller_serializer = SellerSerializer(data=mydata)
        seller_serializer = SellerSerializer(data=request.POST)
        if(seller_serializer.is_valid()):
            seller_serializer.save()
            # return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
            return redirect(sellerview)
        else:
            return HttpResponse("Error in serializer",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("GET method not allowed",status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def seller_view(request):
    if(request.method == "GET"):
        seller = Seller.objects.all()
        seller_serializer = SellerSerializer(seller,many=True)
        return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def login_checkseller(request):
    try:
        getusername = request.POST.get("sellusername")
        getpassword = request.POST.get("sellpassword")
        getuser = Seller.objects.filter(sellusername = getusername,sellpassword = getpassword)
        user_serializer = SellerSerializer(getuser,many=True)
        print(user_serializer)
        if(user_serializer.data):
            for i in user_serializer.data:
                getsellid = i["id"]
                getsellname = i["sellname"]
                getsellusername = i["sellusername"]
            request.session['uid'] = getsellid
            request.session['usellname'] = getsellname
            data = {"sellname":getsellname,"sellusername":getsellusername}
            # return HttpResponse(data)
            return render(request,'seller/templates/sellerprofile.html',{"datas":data})
        else:
            return HttpResponse("Invalid credientials")
    except Manufacturer.DoesNotExist:
        return HttpResponse("Invalid username")
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def sell_viewone(request,id):
    try:
        seller = Seller.objects.get(id=id)
    except Seller.DoesNotExist:
        return HttpResponse("Invlaid ID",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        seller_serializer = SellerSerializer(seller)
        return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
    if(request.method == "PUT"):
        mydata = JSONParser().parse(request)
        seller_serializer = SellerSerializer(seller,data=mydata)
        if(seller_serializer.is_valid()):
            seller_serializer.save()
            return JsonResponse(seller_serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serilaizer",status=status.HTTP_404_NOT_FOUND)
    if(request.method == "DELETE"):
        seller.delete()
        return HttpResponse("Deleted Successfully",status=status.HTTP_200_OK)

@csrf_exempt
def sell_update(request):
    try:
        getshopname = request.POST.get("shop_name")
        getseller = Seller.objects.filter(shop_name=getshopname)
        seller_serializer = SellerSerializer(getseller,many=True)
        return render(request,'updateseller.html',{"data":seller_serializer.data})
    except Seller.DoesNotExist:
        return HttpResponse("Invalid shopname",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def sell_updateaction(request):
    getnewid = request.POST.get("newid")
    getnewseller_name = request.POST.get("newsellname")
    getnewselladdress = request.POST.get("newselladdress")
    getnewshop_name = request.POST.get("newshop_name")
    getnewsellmobile = request.POST.get("newsellmobile")
    getnewsellusername = request.POST.get("newsellusername")
    getnewsellpassword = request.POST.get("newsellpassword")
    mydata = {"sellname":getnewseller_name,"selladdress":getnewselladdress,"shop_name":getnewshop_name,"sellmobile":getnewsellmobile,
    "sellusername":getnewsellusername,"sellpassword":getnewsellpassword}
    jsondata = json.dumps(mydata)
    APIlink = "http://127.0.0.1:8000/manufacturer/sellerone/"+getnewid
    requests.put(APIlink,data=jsondata)
    return redirect(sellerview)

@csrf_exempt
def delete_seller(request):
    try:
        getshopname = request.POST.get("shop_name")
        getseller = Seller.objects.filter(shop_name=getshopname)
        seller_serializer = SellerSerializer(getseller,many=True)
        return render(request,'deleteseller.html',{"data":seller_serializer.data})
    except Seller.DoesNotExist:
        return HttpResponse("Invalid shopname",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def delete_selleraction(request):
    getnewid = request.POST.get("newid")
    APIlink = "http://127.0.0.1:8000/manufacturer/sellerone/"+getnewid
    requests.delete(APIlink)
    return redirect(sellerview)