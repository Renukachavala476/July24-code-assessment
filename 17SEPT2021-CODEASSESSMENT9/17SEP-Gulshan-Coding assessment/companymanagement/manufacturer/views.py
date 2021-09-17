from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from manufacturer.models import *
from manufacturer.serializers import *
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.http import request
import requests
from django.http.response import HttpResponse,JsonResponse
from rest_framework import status
import json

@csrf_exempt
def Manufacturer(request):
    if(request.method == 'POST'):
        manufacturer_serialize = ManuSerializer(data = request.POST)
        if(manufacturer_serialize.is_valid()):
            manufacturer_serialize.save()
            return redirect(login)

def login(request):
    return render(request,'index.html')


@csrf_exempt
def manucheck(request):
    try :
        getuser = request.POST.get('username')
        getpassword = request.POST.get('password')

        getmanu = Manu.objects.filter(username = getuser, password = getpassword  )
        manu_serialize = ManuSerializer(getmanu,many = True)
        print(manu_serialize.data)

        if(manu_serialize.data):
            for i in manu_serialize.data:
                getid = i['id']
                getname = i['name']
                getUsername = i["username"]
                getpassword = i["password"]

            request.session['mid']=getid
            request.session['mname']=getname
            request.session['musername']=getUsername
            request.session['mpassword']=getpassword
            return redirect(dashboard)
        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Manu.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong") 


def dashboard(request):
    try:
        getid = request.session['mid']
        getmanu=Manu.objects.get(id=getid)
        manu_serialize = ManuSerializer(getmanu)
        return render(request,'dashboard.html',{'data':manu_serialize})
    except:
        return HttpResponse('try again')



@csrf_exempt
def CustomerValidation(request):
    if (request.method == "POST"):
        # customer_serializer = CustomerSerializer(request.POST, request.FILES)
        # if(customer_serializer.is_valid()):
            try:
                getName = request.POST.get("customer_name")
                getDOB = request.POST.get("customer_DOB")
                getGender = request.POST.get("gender")
                getAdd = request.POST.get("address")
                getPin = request.POST.get("pincode")
                getMob = request.POST.get("mobileno")
                getEmail = request.POST.get("email")
                getAdhar = request.POST.get("adharno")
                getProduct = request.POST.get("product_type")
                getUsername = request.POST.get("customer_username")
                getPassword = request.POST.get("customer_password")
                getPhoto = request.FILES["customer_photo"]
                getIdproof = request.FILES["customer_idfile"]

                customer_dic = {"customer_name":getName, "customer_DOB":getDOB, "gender":getGender, "address":getAdd, "pincode":getPin, "mobileno": getMob, "email":getEmail, "adharno":getAdhar, "product_type":getProduct, "customer_username":getUsername, "customer_password":getPassword, "customer_photo":getPhoto, "customer_idfile":getIdproof}
                print(customer_dic)
                cus = CustomerSerializer(data=customer_dic)
                print(cus)
                if cus.is_valid():
                    cus.save()
                    
                    return redirect(login)

                else:
                    print(cus.errors)
                return HttpResponse("Successfull")

            except Customer.DoesNotExist:
                return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
            except:
                return HttpResponse("Something went wrong")

@csrf_exempt
def usercheck(request):
    try:
        getuser = request.POST.get("customer_username")
        getpassword = request.POST.get("customer_password")

        getCustomer = Customer.objects.filter(customer_username = getuser, customer_password = getpassword  )
        customer_serializer = CustomerSerializer(getCustomer, many=True)
        print(customer_serializer.data)

        if (customer_serializer.data):
            for n in customer_serializer.data:
                getId = n["id"]
                getName = n["customer_name"]
                getMobile = n["mobileno"]
                getEmail = n["email"]
                getProduct = n["product_type"]
                getAadhar = n["adharno"]
                getUsername = n["customer_username"]
                getPassword = n["customer_password"]
                getPhoto = n["customer_photo"]

            request.session['cid']=getId
            request.session['cname']=getName 
            request.session['cmob']=getMobile
            request.session['cemail']=getEmail
            request.session['cproduct']=getProduct
            request.session['caadhar']=getAadhar
            request.session['cuser']=getUsername
            request.session['cpassword']=getPassword
            request.session['cphoto']=getPhoto

            # cus_data = {"customer_name":getName, "mobileno":getMobile,"email":getEmail,"product_type":getProduct,"adharno":getAadhar,"customer_username":getUsername,"customer_password":getPassword, "customer_photo":getPhoto}
            #return render(request, "customerdashboard.html", {"data":cus_data})
            return redirect(cusDashboard)

        else:
            return HttpResponse("Invalid Credientials", status=status.HTTP_404_NOT_FOUND)

    except Customer.DoesNotExist:
        return HttpResponse("Invalid username or password", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong") 



def cusDashboard(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "customerdashboard.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")

def customerprofile(request):
    try:
        getCid = request.session['cid']
        getcustomer = Customer.objects.get(id=getCid)
        cus_serialiser = CustomerSerializer(getcustomer)

        return render(request, "customerprofile.html", {"data":cus_serialiser.data})

    except:
        return HttpResponse("Try again!")


@csrf_exempt
def deleteapi(request):
    try:
        getflat = request.POST.get("bulding_no")
        getf =Customer.objects.filter(bulding_no=getflat)
        flat_serialize = CustomerSerializer(getf,many=True)
        return render(request,'delete.html',{"data":flat_serialize.data})
    except Customer.DoesNotExist:
        return HttpResponse('Invalid No ')
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def delete_data(request): 
    getno = request.POST.get("newbuilding_no")
    apilink = "http://13.126.238.231:8000/flats/update/"+str(getno)
    requests.delete(apilink)
    # return HttpResponse('Data has deleted successfully')
    return redirect(dashboard)
