from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bank.serializers import BankSerializer
from bank.models import Bank
from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.
@csrf_exempt
def AddPage(request):
    if request.method=="POST":
        getUserName=request.POST.get("username")
        getPassword=request.POST.get("password")
        
        mydict={"username":getUserName,"password":getPassword};
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method allowed")


def bsignin(request):
    return render(request,'bank/signin.html')


      

# def search_customer(request):
#     return render(request,'search.html')              

# @csrf_exempt
# def searchcustomerapi(request):
#     try:
#         getBuildno=request.POST.get("buildingno")
#         getFlat=Flat.objects.filter(buildingno=getBuildno)
#         flat_serialize=FlatSerializer(getFlat,many=True)
#         return render(request,"search.html",{"data":flat_serialize.data})
#         #return JsonResponse(flat_serialize.data,safe=False,status=status.HTTP_200_OK)
#     except Flat.DoesNotExist:
#         return HttpResponse("Invalid Building number",status=status.HTTP_404_NOT_FOUND)  
#     except:
#         return HttpResponse("Something is wrong")
