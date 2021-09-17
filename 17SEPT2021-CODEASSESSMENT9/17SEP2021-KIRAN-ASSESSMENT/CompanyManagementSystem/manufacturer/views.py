from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from manufacturer.serializers import ManufacturerSerializer,SellerSerializer
from manufacturer.models import Manufacturer,Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect
# Create your views here.
@csrf_exempt
def addManufacturer(request): 
    if(request.method=="POST"): 
        mydict=JSONParser().parse(request)
        m_serialize=ManufacturerSerializer(data=mydict)
        if(m_serialize.is_valid()):
            m_serialize.save()
            return JsonResponse(m_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)


def Header(request):
    return render(request,'header.html')

def loginData(request):
    return render(request,'login.html')

@csrf_exempt
def login_check(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getUsers=Manufacturer.objects.filter(username=username,password=password)
        m_serialize=ManufacturerSerializer(getUsers,many=True)
        if(m_serialize.data):
            for i in m_serialize.data:

                a=i["username"]
                b=i["password"]

            request.session['uusername']=a
            request.session['upassword']=b
            return render(request,"header.html")
        else:
            return HttpResponse("Invalid credentails")
    except Student.DoesNotExist:
        return HttpResponse("Invalid Details")




@csrf_exempt
def addSeller(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        s_serialize=SellerSerializer(data=request.POST)
        if(s_serialize.is_valid()):
            s_serialize.save()
            return redirect(viewingSeller)
            #return JsonResponse(s_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def viewSeller(request): 
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        s_serialize=SellerSerializer(sellers,many=True)
        return JsonResponse(s_serialize.data,safe=False)


@csrf_exempt
def sellerDetails(request,id):
    try:
        sellers=Seller.objects.get(id=id)
    except Seller.DoesNotExist:
        return HttpResponse("Invalid Seller Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        s_serialize=SellerSerializer(sellers)
        return JsonResponse(s_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sellers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        s_serialize=SellerSerializer(sellers,data=mydict)
        if(s_serialize.is_valid()):
            s_serialize.save()
            return JsonResponse(s_serialize.data,status=status.HTTP_200_OK)

def SellerAdd(request):
    return render(request,'register.html')

def viewingSeller(request):
    fetchdata=requests.get("http://127.0.0.1:8000/manufacturer/viewall/").json()
    return render(request,'viewseller.html',{"data":fetchdata}) 

def SellerSearch(request):
    return render(request,'search.html')

def SellerUpdate(request):
    return render(request,'editseller.html')

def SellerDelete(request):
    return render(request,'delete.html')


@csrf_exempt
def searchapi(request):
    try:
        getName=request.POST.get("name")
        getname=Seller.objects.get(name=getName)
        s_serialize=SellerSerializer(getname)
        return render(request,"search.html",{"data":s_serialize.data})
        #return JsonResponse(s_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid seller Name")



@csrf_exempt
def update_api(request):
    try:
        getName=request.POST.get("name")
        getname=Seller.objects.get(name=getName)
        s_serialize=SellerSerializer(getname)
        return render(request,"editseller.html",{"data":s_serialize.data})
        #return JsonResponse(s_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid seller Name")

@csrf_exempt
def update_dataread(request):
    getNewId=request.POST.get("newId")
    getName=request.POST.get("newname")
    getAddress=request.POST.get("newaddress")
    getShop_name=request.POST.get("newshop_name")
    getPhone=request.POST.get("newphone_no")
    getUserName=request.POST.get("newusername")
    getPassword=request.POST.get("newpassword")
    mydata={"name":getName,"address":getAddress,"shop_name":getShop_name,"phone_no":getPhone,"username":getUserName,"password":getPassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/manufacturer/view/"+getNewId
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Updated successfully")


@csrf_exempt
def delete_api(request):
    try:
        getName=request.POST.get("name")
        getname=Seller.objects.get(name=getName)
        s_serialize=SellerSerializer(getname)
        return render(request,"delete.html",{"data":s_serialize.data})
        #return JsonResponse(s_serialize.data,safe=False)
    except:
        return HttpResponse("Invalid seller Name")

@csrf_exempt
def delete_dataread(request):
    getNewId=request.POST.get("newId")
    ApiLink="http://127.0.0.1:8000/manufacturer/view/"+getNewId
    requests.put(ApiLink)
    return HttpResponse("Deleted successfully")