from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def studentpage(request):
    if(request.method =="POST"):
        getName=request.POST.get("studentname")
        getAdmnno=request.POST.get("admno")
        getRollno=request.POST.get("Rollno")
        getPname=request.POST.get("parentname")
        getCollege=request.POST.get("collegename")
        mydict={"studentname":getName,"admno":getAdmnno,"Rollno":getRollno,"parentname":getPname,"collegename":getCollege}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")
