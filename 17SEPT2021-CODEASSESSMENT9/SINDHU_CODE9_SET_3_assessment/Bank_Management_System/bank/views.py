from requests.sessions import Request
import json
from django.shortcuts import redirect, render
from bank.models import Bank,Customer
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bank.serializers import BankSerializer,CustomerSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
#####BANK PAGE
@csrf_exempt
def bank_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        bank_serialize=BankSerializer(data=request.POST)
        if(bank_serialize.is_valid()):
            bank_serialize.save()
            # return redirect(viewall_bank_view)
            return JsonResponse(bank_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getbank=Bank.objects.filter(username=username,password=password)
    print(getbank)
    bank_serializer=BankSerializer(getbank,many=True)
    print(bank_serializer.data)
    if(bank_serializer.data):
        for i in bank_serializer.data:
            
            x=i["bankname"]
            y=i["id"]
            print(x)
        request.session["uname"]=x
        request.session["uid"]=y
        return render(request,'adminview.html',{"data":bank_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
def loginviewadmin(request):
    return render(request,'adminlogin.html')
###ADD CUSTOMER
@csrf_exempt
def customer_create(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        customer_serialize=CustomerSerializer(data=request.POST)
        if(customer_serialize.is_valid()):
            customer_serialize.save()
            # return redirect(viewall_bank_view)
            return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
######HTML ADD
def add_customer_view(request):
    return render(request,'add.html')
#######SEARCH,UPDATE,DELETE BACk
@csrf_exempt
def customer_details(request,id):
    try:
        customers=Customer.objects.get(id=id)
        if(request.method=="GET"):
            customer_serializer=CustomerSerializer(customers)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            customer_serialize=CustomerSerializer(customers,data=mydata)
            if(customer_serialize.is_valid()):
                customer_serialize.save()
                return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        if(request.method=="DELETE"):
            customers.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid Id",status=status.HTTP_404_NOT_FOUND)
#####SEARCH API FRONT
def search_customer_view(request):
    return render(request,'search.html')
@csrf_exempt
def searchapi(request):
    try:
        getname=request.POST.get("name")
        getcustomer=Customer.objects.filter(name=getname)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        print(customer_serializer.data)
        # return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"search.html",{"data":customer_serializer.data})
    except Customer.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
######UPDATE FRNT
def update_customer_view(request):
    return render(request,'update.html')
@csrf_exempt
def updateapi(request):
    try:
        getname=request.POST.get("name")
        getcustomer=Customer.objects.filter(name=getname)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        print(customer_serializer.data)
        # return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"update.html",{"data":customer_serializer.data})
    except Customer.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewaddress=request.POST.get("newaddress")
    getnewbankbal=request.POST.get("newbankbal")
    getnewmobileno=request.POST.get("newmobileno")
    getnewusername=request.POST.get("newusername")
    getnewpassword=request.POST.get("newpassword")
    mydata={'name':getnewname,'address':getnewaddress,'bankbal':getnewbankbal,
            'mobileno':getnewmobileno,'username':getnewusername,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/bank/view/" +getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("Data has updated succesfully")
####DELETE
def delete_customer_view(request):
    return render(request,'delete.html')
@csrf_exempt
def deleteapi(request):
    try:
        getname=request.POST.get("name")
        getcustomer=Customer.objects.filter(name=getname)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        print(customer_serializer.data)
        # return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        return render(request,"delete.html",{"data":customer_serializer.data})
    except Customer.DoesNotExist:
        return HttpResponse("Invalid name",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")
@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
    # getnewname=request.POST.get("newname")
    # getnewaddress=request.POST.get("newaddress")
    # getnewbankbal=request.POST.get("newbankbal")
    # getnewmobileno=request.POST.get("newmobileno")
    # getnewusername=request.POST.get("newusername")
    # getnewpassword=request.POST.get("newpassword")
    # mydata={'name':getnewname,'address':getnewaddress,'bankbal':getnewbankbal,
    #         'mobileno':getnewmobileno,'username':getnewusername,'password':getnewpassword}
    # jsondata=json.dumps(mydata)
    # print(jsondata)
    Apilink="http://127.0.0.1:8000/bank/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("Data has been deleted succesfully")

#####VIEWAALL
@csrf_exempt
def customer_list(request):
    if(request.method=="GET"):
        customers=Customer.objects.all()
        customer_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)

def viewall_customer_view(request):
    fetchdata=requests.get("http://127.0.0.1:8000/customer/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})