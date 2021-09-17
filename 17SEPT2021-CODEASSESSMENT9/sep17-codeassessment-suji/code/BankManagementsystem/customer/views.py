from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

     
def addcustomer(request):
    return render(request,'bank/addcustomer.html')   
@csrf_exempt
def customerAddPage(request):
    if request.method=="POST":
        # getName=request.POST.get("name")
        # getAddress=request.POST.get("address")
        # getmobilenumber=request.POST.get("mobilenumber")
        # getBankBalance=request.POST.get("bankbalance")
        # getUserName=request.POST.get("username")
        # getPassword=request.POST.get("password")
        
        # mydict={"name":getName,"address":getAddress,"mobilenumber":getmobilenumber,"bankbalance":getBankBalance,"username":getUserName,"password":getPassword};
        # result=json.dumps(mydict)
        # return HttpResponse(result)
        customer_serialize=CustomerSerializer(data=request.POST)
        if(customer_serialize.is_valid()):
            customer_serialize.save()
            return JsonResponse(customer_serialize.data)
            # return HttpResponse("Success")
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("No get method allowed")


        