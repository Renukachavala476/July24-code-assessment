from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from bank.models import Admin, Customers
from bank.serializers import BankSerializer,AdminSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests,json
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    return render(request,'home.html')
def bank(request):
    return render(request,'index.html')
def viewCustomer(request):
    fetch = requests.get("http://127.0.0.1:8000/bank/viewall/").json()

    return render(request,'views.html',{"data":fetch})
def updateCustomer(request):
    return render(request,'update.html')
def deleteCustomer(request):
    return render(request,'delete.html')
def searchCustomer(request):
    return render(request,'search.html')

def facLogin(request):
    return render(request,'login.html')

def custLogin(request):
    return render(request,'cuslogin.html')

def viewcustProfile(request):

    fetch = requests.get("http://127.0.0.1:8000/bank/viewcust/").json()

    return render(request,'custprofile.html',{"mydata":fetch})


@csrf_exempt
def update_search(request):
    try:
        getMobno = request.POST.get("mobno")
        getMob = Customers.objects.filter(mobno = getMobno )
        admin_serializer = BankSerializer(getMob,many=True)
        return render(request,'update.html',{"data":admin_serializer.data})
        # return JsonResponse(admin_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Customers found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_data(request):
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

@csrf_exempt
def delete_search(request):
    try:
        getMobno = request.POST.get("mobno")
        getMob = Customers.objects.filter(mobno = getMobno )
        admin_serializer = BankSerializer(getMob,many=True)
        return render(request,'delete.html',{"data":admin_serializer.data})
        # return JsonResponse(admin_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)
    

    


@csrf_exempt
def delete_data(request):
    getnewid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/bank/view/"+getnewid
    requests.delete(apilink)
    return HttpResponse("Data deleted Successfully")





@csrf_exempt
def searchapi(request):
    try:
        getMobno = request.POST.get("mobno")
        getCus = Customers.objects.filter(mobno = getMobno )
        admin_serializer = BankSerializer(getCus,many=True)
        return render(request,'search.html',{"data":admin_serializer.data})
        # return JsonResponse(admin_serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def addCustomer(request):
    if(request.method == "POST"):
        # mydata = JSONParser().parse(request)
        admin_serializer = BankSerializer(data = request.POST)
        if(admin_serializer.is_valid()):
            admin_serializer.save()
            return redirect(viewCustomer)
        else:
            return HttpResponse("Error in Serialization")

    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewall(request):
    if(request.method == "GET"):
        flats = Customers.objects.all()
        admin_serializer = BankSerializer(flats, many=True)
        return JsonResponse(admin_serializer.data, safe=False)


@csrf_exempt
def viewCust(request):
    if(request.method == "GET"):
        a = Customers.objects.all()
        adm_serializer = BankSerializer(a, many=True)
        return JsonResponse(adm_serializer.data, safe=False)

@csrf_exempt
def view(request,id):
    try:
        bank = Customers.objects.get(id = id)
        if(request.method == "GET"):
            admin_serializer = BankSerializer(bank)
            return JsonResponse(admin_serializer.data, safe=False)

        if(request.method == "DELETE"):
            bank.delete()
            return HttpResponse("Customer Deleted Successfully")

        if(request.method == "PUT"):
            mydict = JSONParser().parse(request)
            bnk_serialize = BankSerializer(bank, data = mydict)
            if(bnk_serialize.is_valid()):
                bnk_serialize.save()
                return JsonResponse(bnk_serialize.data, status=status.HTTP_200_OK)

    except Customers.DoesNotExist:
        return HttpResponse("Invalid Customer id",status=status.HTTP_404_NOT_FOUND)

       
@csrf_exempt
def login_check(request):
   
    try:
        username = request.POST.get("aname")
        password = request.POST.get("pwd")

        getUser = Admin.objects.filter(aname = username, pwd=password)
        a_serializer = AdminSerializer(getUser, many=True)
        if(a_serializer.data):
            for i in a_serializer.data:
                x = i["aname"]
                print(x)
            request.session['admname'] = x
            
            return render(request, 'head.html')

        else:
          
            return HttpResponse("Invalid Credentials")

    except Admin.DoesNotExist:
        return HttpResponse("User not found")



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



@csrf_exempt
def addAdmin(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        admin_serializer = AdminSerializer(data = mydata)
        if(admin_serializer.is_valid()):
            admin_serializer.save()
            return JsonResponse(admin_serializer.data)
        else:
            return HttpResponse("Error in Serialization")

    else:
        return HttpResponse("GET method not allowed")







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



def logout_admin(request):
        logout(request)
       
        return render(request,'login.html') 


def logout_customer(request):
        logout(request)
        return render(request,'cuslogin.html') 