from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from faculty.serializers import FacultySerializer
import json
from faculty.models import Faculty
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from django import forms
@csrf_exempt
def facultyaddpage(request):
    if (request.method=="POST"):
        gcode=request.POST.get("faculty_code")
        gname=request.POST.get("name")
        gaddress=request.POST.get("address")
        gmobilenumber=request.POST.get("mobilenumber")
        gdepartment=request.POST.get("department")
        mydict={'faculty_code':gcode,'name':gname,'address':gaddress,'mobilenumber':gmobilenumber,'department':gdepartment}
        faculty_serialize=FacultySerializer(data=mydict)
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
    # if (request.method=="POST"):
    #     student_serialize=StudentSerializer(data=request.POST)
    #     if (student_serialize.is_valid()):
    #         student_serialize.save()
    #         return redirect(stu_view)
    #     else:
    #         return HttpResponse("error in serialisation",status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)
    

@csrf_exempt
def faculty_list(request):
    if (request.method=="GET"):
        faculty=Faculty.objects.all()
        faculty_serializer=FacultySerializer(faculty,many=True)
        return JsonResponse(faculty_serializer.data,safe=False)
@csrf_exempt
def faculty_details(request,fetchid):
    try:
        faculty=Faculty.objects.get(id=fetchid)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        faculty_serializer=FacultySerializer(students)
        return JsonResponse(faculty_serializer.data,safe=False)
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        faculty_serialize=FacultySerializer(faculty,data=mydict)
        if (faculty_serialize.is_valid()):
            faculty_serialize.save()
            return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(faculty_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    if(request.method=="DELETE"):
        faculty.delete()
        return HttpResponse("Deleted",status=status.HTTP_404_NOT_FOUND)


def faculty_view(request):
    return render(request,'index.html')

def fac_view(request):
    fetchdata=requests.get("http://localhost:8000/faculty/viewall/").json()
    return render(request,'viewall.html',{"data":fetchdata})

def search_view(request):
    return render(request,'search.html')

def update_view(request):
    return render(request,'update.html')

def delete_view(request):
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')


@csrf_exempt
def searchapi(request):
    try:
        getfaculty_code=request.POST.get("faculty_code")
        getfaculty=Faculty.objects.filter(faculty_code=getfaculty_code)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,"search.html",{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def updatesearchapi(request):
    try:
        gfaculty_code=request.POST.get("faculty_code")
        getfaculty=Faculty.objects.filter(faculty_code=gfaculty_code)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,'update.html',{"data":faculty_serializer.data})
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")


@csrf_exempt
def update_data_read(request):
    gfaculty_code=request.POST.get("newfaculty_code")
    gname=request.POST.get("newname")
    getid=request.POST.get("newid")
    gaddress=request.POST.get("newaddress")
    gmobilenumber=request.POST.get("newmobilenumber")
    gdepartment=request.POST.get("newdepartment")
    mydata={'faculty_code':gfaculty_code,'name':gname,'mobilenumber':gmobilenumber,'address':gaddress,'mobilenumber':gmobilenumber,'department':gdepartment}
    jsondata=json.dumps(mydata)
    Apilink="http://localhost:8000/faculty/viewfaculty/" + getid
    print(jsondata)
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data updated successfully")


@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
   
    Apilink="http://localhost:8000/faculty/viewfaculty/" + getnewid
    requests.delete(Apilink)
    return HttpResponse("data deleted successfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        gcode=request.POST.get("faculty_code")
        getfaculty=Faculty.objects.filter(faculty_code=gcode)
        faculty_serializer=FacultySerializer(getfaculty,many=True)
        return render(request,"delete.html",{"data":faculty_serializer.data})
       
        return HttpResponse("Invalid data",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("invalid")

@csrf_exempt
def checklogin(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getuser=Faculty.objects.filter(username=username,password=password)
        faculty_serialize=FacultySerializer(getuser,many=True)
        if(faculty_serialize.data):
            for i in faculty_serialize:
                x=i["name"]
                y=i["id"]
            request.session['uname']=x 
            request.session['uid']=y 
            return render(request,"welcome.html")
        else:
            return HttpResponse("invalid data")
    except Faculty.DoesNotExist:
        return HttpResponse("invalid data")
    






