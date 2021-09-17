from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from manufacturer.serializers import SellerSerializer
from manufacturer.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests,json
from django.shortcuts import redirect
from manufacturer.views import SellerSerializer

from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm
from django.urls import reverse_lazy
# Create your views here.

def login_Data(request):
    return render(request,'loggin.html')


@csrf_exempt
def logincheck(request):
    try:
        username=request.POST.get("username")
        password=request.POST.get("password")
        getUsers=Seller.objects.filter(username=username,password=password)
        s_serialize=SellerSerializer(getUsers,many=True)
        if(s_serialize.data):
            for i in s_serialize.data:
                a=i["name"]
                b=i["id"]
                c=i["address"]
                d=i["shop_name"]
                e=i["phone_no"]
                f=i["username"]
                g=i["password"]
            request.session['uname']=a
            request.session['uid']=b
            request.session['uaddress']=c
            request.session['ushop_name']=d
            request.session['uphone_no']=e
            request.session['uusername']=f
            request.session['upassword']=g
            return render(request,"base.html")
        else:
            return HttpResponse("Invalid credentails")
    except Student.DoesNotExist:
        return HttpResponse("Invalid Details")


@csrf_exempt
def addSeller(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        s_serialize=SellerSerializer(data=request.POST)
        if(s_serialize.is_valid()):
            s_serialize.save()
            return redirect(viewingSeller)
            #return JsonResponse(s_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method allowed",status=status.HTTP_404_NOT_FOUND)



def ProfileData(request):
    return render(request,'profile.html')

def PasswordChange(request):
    return render(request,'change_password.html')

def PasswordChangeDone(request):
    return render(request,'change_password_done.html')

@csrf_exempt
def MyPasswordChangeView(request):
    context={}
    if request.method=="POST":
        current=request.POST["cpassword"]
        new_pass=request.POST["npassword"]
        user=Seller.objects.get(id=request.user.id)
        check=user.match_password(current)
        if  check==True:
            user.set_password(new_pass)
            context["msz"]="password changed Successfully"
            context["col"]="alert-success"            
        else:
            context["msz"]="incorrect"
            context["col"]="alert-danger"
    return render(request,"change_password.html",context)

# def MyPasswordResetDoneView(PasswordResetDoneView):
#     template_name='change_password_done.html'