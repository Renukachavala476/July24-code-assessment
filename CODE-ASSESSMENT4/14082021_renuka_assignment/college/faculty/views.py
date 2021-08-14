from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def facultypage(request):
    if(request.method =="POST"):
        getName=request.POST.get("facultyname")
        getAddress=request.POST.get("address")
        getDepartment=request.POST.get("department")
        getCollege=request.POST.get("college")
        mydict={"facultyname":getName,"address":getAddress,"department":getDepartment,"college":getCollege}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")
