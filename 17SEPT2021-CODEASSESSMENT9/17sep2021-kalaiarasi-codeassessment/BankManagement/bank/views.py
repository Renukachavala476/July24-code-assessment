from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from requests.sessions import Request
from bank.serializers import CustomerSerializer, AdminSerializer
from bank.models import Customer, Admin
from rest_framework.parsers import JSONParser
from django.contrib.auth import logout
from rest_framework import status
import requests
# Create your views here.


def addata(request):
    return render(request,"index.html")

def viewall(request):
    fetchdata=requests.get("http://127.0.0.1:8000/bank/viewall/").json()
    return render(request,"viewcustomer.html",{"data":fetchdata})

def searchcode(request):
    return render(request,"searchcustomer.html")


def updation(request):
    return render(request,"updatecustomer.html")

def updationcus(request):
    return render(request,"updateprofile.html")

def deletion(request):
    return render(request,"deletecustomer.html")



@csrf_exempt
def addcustomer(request):
    if(request.method=="POST"):
        
        # mydict=JSONParser().parse(request)
        customer_serialize=CustomerSerializer(data=request.POST)
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return redirect(viewall)
            return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def customer_list(request):
    if(request.method=="GET"):
        customers=Customer.objects.all()
        customer_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)


@csrf_exempt
def customer_details(request, id):
    try:
        customers=Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        customer_serializer=CustomerSerializer(customers)
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        customers.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        customer_serialize=CustomerSerializer(customers,data=mydict)
        if (customer_serialize.is_valid()):
            customer_serialize.save()
            return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
        


@csrf_exempt
def searchapi(request):
    try:
        getmob=request.POST.get("mobnum")
        getcustomer=Customer.objects.filter(mobnum=getmob)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        return render(request,"searchcustomer.html",{"data":customer_serializer.data})
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)

    except Customer.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def updatesearchapi(request):
    try:
        getmob=request.POST.get("mobnum")
        getcustomer=Customer.objects.filter(mobnum=getmob)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        return render(request,"updatecustomer.html",{"data":customer_serializer.data})
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Customer.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt       

def updatedataread(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewadd=request.POST.get("newadd")
    getnewbal=request.POST.get("newbal")
    getnewmob=request.POST.get("newmob")
    getnewuser=request.POST.get("newuser")
    getnewpass=request.POST.get("newpass")

    mydata={'id':getnewid,'name':getnewname,'address':getnewadd,'bankbalance':getnewbal,'mobnum':getnewmob,'username':getnewuser,'password':getnewpass}
    jsondata=json.dumps(mydata)
    apilink="http://127.0.0.1:8000/bank/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getmob=request.POST.get("mobnum")
        getcustomer=Customer.objects.filter(mobnum=getmob)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        return render(request,"deletecustomer.html",{"data":customer_serializer.data})
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)

    except Customer.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def deletedataread(request):
    getnewid=request.POST.get("newid")

    apilink="http://127.0.0.1:8000/bank/viewone/" + getnewid
    requests.delete(apilink)
    return HttpResponse("data deleted successfully")



####admin###



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
        return render(request,'header.html',{"data":admin_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
      


 


def loginviewadmin(request):
    return render(request,'adminlogin.html')

def logout_admin(request):
        logout(request)
        
        template='adminlogin.html'
        return render(request,template)     

@csrf_exempt
def login_checkcustomer(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getcus=Customer.objects.filter(username=username,password=password)
    customer_serializer=CustomerSerializer(getcus,many=True)
    if(customer_serializer.data):
        for i in customer_serializer.data:
            x=i["name"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'headerc.html',{"data":customer_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
      


 


def loginviewcustomer(request):
    return render(request,'customerlogin.html')

def logout_customer(request):
        logout(request)
        
        template='customerlogin.html'
        return render(request,template)     




@csrf_exempt
def updatesearchapic(request):
    try:
        getmob=request.POST.get("mobnum")
        getcustomer=Customer.objects.filter(mobnum=getmob)
        customer_serializer=CustomerSerializer(getcustomer,many=True)
        return render(request,"updateprofile.html",{"data":customer_serializer.data})
        return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
   
    except Customer.DoesNotExist:
        return HttpResponse("invalid",status=status.HTTP_404_NOT_FOUND)
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt       

def updatedatareadc(request):
    getnewid=request.POST.get("newid")
    getnewname=request.POST.get("newname")
    getnewadd=request.POST.get("newadd")
    getnewbal=request.POST.get("newbal")
    getnewmob=request.POST.get("newmob")
    getnewuser=request.POST.get("newuser")
    getnewpass=request.POST.get("newpass")

    mydata={'id':getnewid,'name':getnewname,'address':getnewadd,'bankbalance':getnewbal,'mobnum':getnewmob,'username':getnewuser,'password':getnewpass}
    jsondata=json.dumps(mydata)
    apilink="http://127.0.0.1:8000/bank/viewone/" + getnewid
    requests.put(apilink,data=jsondata)
    return HttpResponse("data updated successfully")