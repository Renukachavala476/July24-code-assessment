from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.serializers import raise_errors_on_nested_writes
from bank.models import *
from bank.serializer import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import request
import requests
from django.http.response import HttpResponse,JsonResponse
from rest_framework import status
import json


@csrf_exempt
def bankAdmin(request):
    if (request.method=="POST"):
        
        mydata=JSONParser().parse(request)
        bank_serialize=BankSerializer(data=mydata)
        
        if (bank_serialize.is_valid()):
            bank_serialize.save()
            
            return JsonResponse(bank_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getbank=Bankapp.objects.filter(username=username,password=password)
    bank_serializer=BankSerializer(getbank,many=True)
    if(bank_serializer.data):
        for i in bank_serializer.data:
            x=i["username"]
            y=i["id"]
            print(x)
        request.session['username']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":bank_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
        #return render(request,'invalidpage.html')


def loginviewbank(request):
    return render(request,"adminlogin.html")

def logout_bank(request):
        logout_bank(request)
        
        template='adminlogin.html'
        return render(request,template)


@csrf_exempt
def AddCustomer(request):
    if (request.method == "POST"):

        try:
            getname = request.POST.get("name")
            getaddress = request.POST.get("address")
            getbank_balance = request.POST.get("bank_balance")
            getmobile = request.POST.get("mobile")
            getusername = request.POST.get("username")
            getpassword = request.POST.get("password")
            getcustomer = Bankapp.objects.filter(name=getname, address=getaddress, bank_balance=getbank_balance, mobile=getmobile, username=getusername, password=getpassword)
            bank_serializer = BankSerializer(getcustomer, many=True)
            print(bank_serializer.data)
            if (bank_serializer.data):
                return HttpResponse("donor Already Exists")
            else:
                bank_serializer = BankSerializer(data=request.POST)
                if (bank_serializer.is_valid()):
                    bank_serializer.save()  #Save to Db
                    #return redirect(loginview)
                    return redirect(viewall)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
        except Bankapp.DoesNotExist:
            return HttpResponse("Invalid username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


def register(request):
    return render(request,'register.html')


def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/adminss/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

@csrf_exempt
def Viewcustomerall(request):
    if(request.method=="GET"):
        bank=Bankapp.objects.all()
        bank_serializer=BankSerializer(bank,many=True)
        return JsonResponse(bank_serializer.data,safe=False)



def search_customer(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getusername=request.POST.get("username")
        getusers=Bankapp.objects.filter(username=getusername)
        bank_serialize=BankSerializer(getusers,many=True)
        return render(request,"search.html",{"data":bank_serialize.data})
    except:   
        return HttpResponse("Invalid Username",status=status.HTTP_404_NOT_FOUND)


def update(request):
    return render(request,'updatee.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getusername=request.POST.get("username")
        getusers=Bankapp.objects.filter(username=getusername)
        bank_serializer=BankSerializer(getusers,many=True)
        return render(request,"search.html",{"data":bank_serializer.data}) 
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")

        getname = request.POST.get("newname")
        getaddress = request.POST.get("newaddress")
        getbank_balance = request.POST.get("newbank_balance")
        getmobile = request.POST.get("newmobile")
        getusername = request.POST.get("newusername")
        getpassword = request.POST.get("newpassword")
       
        
        mydata={'name':getname,'address':getaddress,'bank_balance':getbank_balance,'mobile':getmobile,'username':getusername,'password':getpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/adminss/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(viewall) 
        #return HttpResponse("data has be updated successfully")


def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/adminss/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getuser=request.POST.get("username")
        getusername=Bankapp.objects.filter(username=getuser)
        bank_serializer=BankSerializer(getusername,many=True)
        return render(request,"delete.html",{"data":bank_serializer.data})
    except:   
        return HttpResponse("Invalid Username")



@csrf_exempt
def ViewCustomer(request,id):
    try:
        d1=Bankapp.objects.get(id=id)
        if(request.method=="GET"):
            bank_serializer=BankSerializer(d1)
            return JsonResponse(bank_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            d1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            bank_serializer=BankSerializer(d1,data=mydata)
            if(bank_serializer.is_valid()):
                bank_serializer.save()
                return JsonResponse(bank_serializer.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(bank_serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Bankapp.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)

