from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from manufacturer.models import Manufacturer,Seller
from manufacturer.serializers import ManufacturerSerializer,SellerSerializer


@csrf_exempt
def addmanufacturer(request):
    if (request.method=="POST"):
        
        mydata=JSONParser().parse(request)
        admin_serialize=ManufacturerSerializer(data=mydata)
        
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
    getadmin=Manufacturer.objects.filter(username=username,password=password)
    admin_serializer=ManufacturerSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["username"]
            y=i["id"]
            print(x)
        request.session['uusername']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":admin_serializer.data})
    else:
        return HttpResponse("Invalid Credentials")
        #return render(request,'invalidpage.html')


 


def loginviewadmin(request):
    return render(request,"adminlogin.html")

def logout_admin(request):
        logout(request)
        
        template='adminlogin.html'
        return render(request,template)


@csrf_exempt
def Addseller(request):
    if (request.method == "POST"):

        try:
            getname = request.POST.get("name")
            getaddress = request.POST.get("address")
            getsname = request.POST.get("sname")
            getmobile = request.POST.get("mobile")
            getusername = request.POST.get("username")
            getpassword = request.POST.get("password")
            getCustomer = Seller.objects.filter(username=getusername)
            customer_serialiser = SellerSerializer(getCustomer, many=True)
            print(customer_serialiser.data)
            if (customer_serialiser.data):
                
                return HttpResponse("customer Already Exists")


            else:
                customer_serialize = SellerSerializer(data=request.POST)
                if (customer_serialize.is_valid()):
                    customer_serialize.save()  #Save to Db
                    #return redirect(loginview)
                    return redirect(viewall)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
        except Seller.DoesNotExist:
            return HttpResponse("Invalid username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/manufacturer/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

@csrf_exempt
def ViewCustomerall(request):
    if(request.method=="GET"):
        customer=Seller.objects.all()
        customer_serializer=SellerSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)



def search_customer(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Seller.objects.filter(username=getnumber)
        customer_serialize=SellerSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid Username",status=status.HTTP_404_NOT_FOUND)





def update(request):
    return render(request,'updatee.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Seller.objects.filter(username=getnumber)
        customer_serialize=SellerSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":customer_serialize.data}) 
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")

        getname = request.POST.get("newname")
        getaddress = request.POST.get("newaddress")
        getsname = request.POST.get("newsname")
        getmobile = request.POST.get("newmobile")
        getusername = request.POST.get("newusername")
        getpassword = request.POST.get("newpassword")
       
        
        mydata={'name':getname,'address':getaddress,'mobile':getmobile,'username':getusername,'password':getpassword}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/manufacturer/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(viewall) 
        #return HttpResponse("data has be updated successfully")


def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/manufacturer/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getnumber=request.POST.get("username")
        getnumbers=Seller.objects.filter(username=getnumber)
        customer_serialize=SellerSerializer(getnumbers,many=True)
        return render(request,"delete.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid Username")



@csrf_exempt
def ViewCustomer(request,id):
    try:
        c1=Seller.objects.get(id=id)
        if(request.method=="GET"):
            customer_serializer=SellerSerializer(c1)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            c_serial=SellerSerializer(c1,data=mydata)
            if(c_serial.is_valid()):
                c_serial.save()
                return JsonResponse(c_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(c_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Seller.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)

