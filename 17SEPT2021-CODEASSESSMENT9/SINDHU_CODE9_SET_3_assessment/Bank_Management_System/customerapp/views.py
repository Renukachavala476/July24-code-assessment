from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from bank.models import Customer
from bank.serializers import CustomerSerializer
from django.contrib.auth import logout


# Create your views here.

@csrf_exempt
def login_check1(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getname=Customer.objects.filter(username=username,password=password)
    customer_serializer=CustomerSerializer(getname,many=True)
    if(customer_serializer.data):
        for i in customer_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminview2.html',{"data":customer_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
def loginviewadmin1(request):
    return render(request,'adminlogin2.html')

def logout_admin(request):
        logout(request)
        template='adminlogin2.html'
        return render(request,template)   


def myViewAllPage2(request):
    fetchdata=requests.get("http://127.0.0.1:8000/customerapp/viewallcust2/").json()
    return render(request,'viewall.html',{"data":fetchdata})

@csrf_exempt
def myCustomerList2(request):
    if(request.method=="GET"):
        customers=Customer.objects.all()
        customer_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)

def myUpdate2(request):
    return render(request,'update2.html')

@csrf_exempt
def UpdateRead2(request):
    getNewId=request.POST.get("newid")
    getNewname=request.POST.get("newname")
    # getNewaddress=request.POST.get("newaddress")
    # getNewbankbal=request.POST.get("newbankbal")
    # getNewmobilenumber=request.POST.get("newmobilenumber")
    # getNewusername=request.POST.get("newusername")
    getNewpassword=request.POST.get("newpassword")
    # mydata={'name':getNewname,'address':getNewaddress,'bankbal':getNewbankbal,'mobilenumber':getNewmobilenumber,'username':getNewusername,'password':getNewpassword}
    mydata={'name':'getNewname','password':'getNewpassword'}
    print(mydata)
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/customerapp/viewseller2/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return HttpResponse("Password Changed!!!")
    

@csrf_exempt
def UpdateSearchAPI2(request):
    try:
        getname=request.POST.get("name")
        getaddress=Customer.objects.filter(name=getname)
        customer_serializer=CustomerSerializer(getaddress,many=True)
        return render(request,"update2.html",{"data":customer_serializer.data})
        #return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def myCustomerDetails2(request,id):
    customers=Customer.objects.get(id=id)
    if (request.method=="PUT"):  
            mydata=JSONParser().parse(request)
            customer_serialize=CustomerSerializer(customerrs,data=dict)
            if(customer_serialize.is_valid()):
                customer_serialize.save()
                return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serialize.errors,status=status.HTTP_400_BAD_REQUEST)