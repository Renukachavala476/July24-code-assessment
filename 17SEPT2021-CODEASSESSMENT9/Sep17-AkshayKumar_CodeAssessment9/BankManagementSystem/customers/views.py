from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from customers.models import Customers
from bank.serializers import BankSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests,json
from django.contrib import messages
from django.contrib.auth import logout




def custLogin(request):
    return render(request,'cuslogin.html')

def viewcustProfile(request):

    fetch = requests.get("http://127.0.0.1:8000/bank/viewcust/").json()

    return render(request,'custprofile.html',{"mydata":fetch})


@csrf_exempt
def viewCust(request):
    if(request.method == "GET"):
        a = Customers.objects.all()
        adm_serializer = BankSerializer(a, many=True)
        return JsonResponse(adm_serializer.data, safe=False)

@csrf_exempt
def update_custsearch(request):
    try:
        getMobno = request.POST.get("mobno")
        getMob = Customers.objects.filter(mobno = getMobno )
        admin_serializer = BankSerializer(getMob,many=True)
        return render(request,'custupdate.html',{"data":admin_serializer.data})
        # return JsonResponse(admin_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Customers found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_custdata(request):
    getnewid = request.POST.get("newid")
    getname = request.POST.get("newbuildingno")
    getaddress = request.POST.get("newaddress")
    getbankbalance = request.POST.get("newbankbalance")
    getmobno = request.POST.get("newmobno")
    getusername= request.POST.get("newusername")
    getpassword = request.POST.get("newpassword")
    mydata= {"name":getname,"address":getaddress,"bankbalance":getbankbalance,"mobno":getmobno,"username":getusername,"password":getpassword}
    jsondata = json.dumps(mydata)
    apilink = "http://127.0.0.1:8000/bank/view/"+getnewid
    requests.put(apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")

def updatecustpwd(request):
    return render(request,'custupdate.html')


def logout_customer(request):
        logout(request)
        return render(request,'cuslogin.html') 


@csrf_exempt
def custlogin_check(request):
   
    try:
        username = request.POST.get("username")
        password = request.POST.get("password")

        getCust = Customers.objects.filter(username = username, password=password)
        a_serializer = BankSerializer(getCust, many=True)
        if(a_serializer.data):
            for i in a_serializer.data:
                x = i["name"]
                print(x)
            request.session['custname'] = x
            
            return render(request, 'custhead.html')

        else:
          
            return HttpResponse("Invalid Credentials")

    except Customers.DoesNotExist:
        return HttpResponse("Customer not found")