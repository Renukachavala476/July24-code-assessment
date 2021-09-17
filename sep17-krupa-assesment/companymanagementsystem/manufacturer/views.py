from re import search
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import requests
from manufacturer.models import seller,Sign
from manufacturer.serializers import sellerSerializer,SignSerializer
from rest_framework import status
import json

# Create your views here.

def mainpage(request):
    return render(request,'main.html')

def login(request):
    return render(request,'login.html')

def homepage(request):
    return render(request,'home.html')

def search_c(request):
    return render(request,'search.html')

def update(request):
    return render(request,'update.html')


def delete(request):
    return render(request,'delete.html')


def add_customer(request):
    return render(request,'add.html')

def view_customer(request):
    x=requests.get("http://127.0.0.1:8000/manufacture/viewall/").json()
    return render(request,'view.html',{"data":x})

@csrf_exempt
def search_customer(request):
    try:
        getname=request.POST.get("mno")
        print(getname)
        getcustomer=seller.objects.filter(mno=getname)
        customer_serial=sellerSerializer(getcustomer,many=True)
        return render(request,"search.html",{"data":customer_serial.data})

        # return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

    except seller.DoesNotExist:
        return HttpResonse("Invalid customer name",status=status.HTTP_404_NOT_FOUND)
    except: 
        return HttpResponse("something went wrong",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        # mydit=JSONParser().parse(request)
        customer_serial=sellerSerializer(data=request.POST)
        if (customer_serial.is_valid()):
            customer_serial.save()
            return JsonResponse(customer_serial.data,status=status.HTTP_200_OK)
    
        else:
            return HttpResponse("error in serilazation",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("ERROR",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def viewcustomer(request):
    if(request.method=="GET"):
        c1=seller.objects.all()
        customer_serial=sellerSerializer(c1,many=True)
        return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def update_d(request,fetchid):
    try:
        c1=seller.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serial=sellerSerializer(c1)
            return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydit=JSONParser().parse(request)
            customer_serial=sellerSerializer(c1,data=mydit)
            if (customer_serial.is_valid()):
                customer_serial.save()
                return JsonResponse(customer_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except seller.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)         

@csrf_exempt
def update_api(request):
    try:
        getna=request.POST.get("mno")
        print(getna)
        getdata=seller.objects.filter(mno=getna)
        customer_serial=sellerSerializer(getdata,many=True)
        return render(request,"update.html",{"data":customer_serial.data})

    except seller.DoesNotExist:
        return HttpResonse("Invalid name",status=status.HTTP_404_NOT_FOUND)

    except: 
        return HttpResponse("error",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data(request):
    getid=request.POST.get("newid")

    getname=request.POST.get("newname")
    getadress=request.POST.get("newaddress")
    getphno=request.POST.get("newmno")
    getshop=request.POST.get("newshop")
    getuser=request.POST.get("newuser")
    getpass=request.POST.get("newpass")

    mydata={'name':getname,'address':getadress,'id':getid,'shopname':getshop,'username':getuser,'password':getpass}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/manufacture/view/" + getid
    requests.put(Apilink, data=jsondata)
    return HttpResponse("data has updated sucessfuly")




@csrf_exempt
def deleteapi(request):
    try:
        getbno=request.POST.get("mno")
        getc=seller.objects.filter(mno=getbno)
        customer_serial=sellerSerializer(getc,many=True)
        return render(request,"delete.html",{"data":customer_serial.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except seller.DoesNotExist:
        return HttpResponse("Invalid number",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def delete_data(request):
    getid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/manufacture/view/"+getid
    requests.delete(Apilink)
    return HttpResponse("data has deleted sucessfully")


@csrf_exempt
def usercheck(request):
    try:
        getuser = request.POST.get("username")
        getpassword = request.POST.get("password")

        getCustomer = Sign.objects.filter(username = getuser,password = getpassword  )
        customer_serializer = SignSerializer(getCustomer, many=True)
        print(customer_serializer.data)

        if (customer_serializer.data):
            for i in customer_serializer.data:
                a=i["name"]
                b=i["address"]
                c=i["shopname"]
                d=i["mno"]
                e=i["id"]         

            request.session['cid']=e
            request.session['cname']=a
            request.session['caddress']=b
            request.session['cshopname']=c
            request.session['cmno']=d
        
            return redirect(add_customer)

        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Sign.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong") 
