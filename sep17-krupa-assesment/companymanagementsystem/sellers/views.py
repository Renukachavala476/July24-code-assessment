
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from sellers.serializers import sellerSerializer
from sellers.models import seller
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.
 
@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getUsers = seller.objects.filter(username=getUsername, password=getPassword)
        user_serialiser = sellerSerializer(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                a=i["name"]
                b=i["address"]
                c=i["shopname"]
                d=i["mno"]
                e=i["id"]         

            request.session['cid']=e
            request.session['cname']=a
            request.session['caddress']=b
            request.session['cshopname']=c
            request.session['cmno']=d
            # Session set 
           
            #Session      
            return render(prof_view,"profile.html")
        else:
            return HttpResponse("Invalid Credentials")               
    except seller.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")
        

@csrf_exempt
def profile(request):
    # if (request.method=="GET"):
        try:
            getUid = request.session['cid']
            getUsers = seller.objects.get(id=getUid)
            user_serialiser = sellerSerializer(getUsers)
            
        except seller.DoesNotExist:
            return render(request, 'profile.html',{"data":user_serialiser.data})    
        except:
            return HttpResponse("Something went wrong....")  


def loginview(request):
    return render(request, 'login.html')
def logout(request):
    return render(request, 'logout.html') 

def forgot(request):
    return render(request, 'forgot.html')  

def head(request):
    return render(request, 'header.html') 
def profile(request):
    return render(request, 'profile.html') 

@csrf_exempt
def user_create(request):
    if (request.method == "POST"):

        try:
            getUsername = request.POST.get("username")
            getPassword = request.POST.get("password")
            getUsers = seller.objects.filter(username=getUsername)
            user_serialiser = sellerSerializer(getUsers, many=True)
            print(user_serialiser.data)
            if (user_serialiser.data):
                
                return HttpResponse("User Already Exists")


            else:
                user_serialize = sellerSerializer(data=request.POST)
                if (user_serialize.is_valid()):
                    user_serialize.save()  #Save to Db
                    return redirect(loginview)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)          
            
        except seller.DoesNotExist:
            return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")    
   
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def update_data(request):
    getid=request.POST.get("newid")
    getpass=request.POST.get("newpass")

    mydata={'id':getid,'password':getpass}
    jsondata=json.dumps(mydata)
    print(jsondata)
    Apilink="http://127.0.0.1:8000/seller/view/" + getid
    requests.put(Apilink, data=jsondata)
    return HttpResponse("data has updated sucessfuly")

@csrf_exempt
def update_d(request,fetchid):
    try:
        c1=seller.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serial=sellerSerializer(c1)
            return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method=="PUT"):
            mydit=JSONParser().parse(request)
            customer_serial=sellerSerializer(c1,data=mydit)
            if (customer_serial.is_valid()):
                customer_serial.save()
                return JsonResponse(customer_serial.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    except seller.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)         


@csrf_exempt
def viewcustomer(request):
    if(request.method=="GET"):
        c1=seller.objects.all()
        customer_serial=sellerSerializer(c1,many=True)
        return JsonResponse(customer_serial.data,safe=False,status=status.HTTP_200_OK)
