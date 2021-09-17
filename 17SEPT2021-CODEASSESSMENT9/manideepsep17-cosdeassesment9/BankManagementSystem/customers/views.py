from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from customers.models import AddloginModel
from customers.serializers import loginSerializer
import requests
from rest_framework import status











@csrf_exempt
def Login(request):
    if request.method=="POST":
        print(1)
        username=request.POST.get('username')
        password1=request.POST.get('password')
        flag=0
        data=RegisterModel.objects.filter(email=username,password=password1)
        print(data)
        if data:
            userserialiser=RegisterSerializer(data,many=True)
            request.session['user']=userserialiser.data
            print(request.session['user'])
            a="login"
            return redirect(Index)
    return render(request,'login.html')
