from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from bank.models import bank,AdminRegisterModel,AdminloginModel
from bank.serializers import bankSerializer,AdminRegisterSerializer,AdminloginSerializer
import requests
from rest_framework import status

def addcust(request):
    return render(request,"addcust.html")

def searchcustomer(request):
    return render(request,"search.html")


# def veiwallevents(request):
#     fetchdata=requests.get("http://127.0.0.1:8000/events/viewall/").json()
#     return render(request,"viewall.html",{"data":fetchdata})

def updatecustomer(request):
    return render(request,"edit.html")

def deletecustomer(request):
    return render(request,"delete.html")






@csrf_exempt
def addcustomers(request):
    if(request.method=='POST'):
        bank_serialize=bankSerializer(data=request.POST)
        if(bank_serialize.is_valid()):
            bank_serialize.save()
            return JsonResponse(bank_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("sucess")

@csrf_exempt

def bank_list(request):
    if(request.method=="GET"):
        banks=bank.objects.all()
        bank_serializer=bankSerializer(banks,many=True)
        return JsonResponse(bank_serializer.data,safe=False)


@csrf_exempt
def mycust(request,fetchid):
    try:
        bank1=bank.objects.get(id=fetchid)
        if(request.method=="GET"):
            bank_serializer=bankSerializer(bank1)
            return JsonResponse(bank_serializer.data,safe=False)

        if(request.method=="DELETE"):
            bank1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            custdata=JSONParser().parse(request)
            bank_serialize=bankSerializer(bank1,data=custdata)
            if (bank_serialize.is_valid()):
                bank_serialize.save()
                return JsonResponse(bank_serialize.data)
            else:
                return JsonResponse(bank_serialize.errors)
    except bank.DoesNotExist:
        return HttpResponse("invalid syntax")


@csrf_exempt
def searchapi(request):
    try:
        getname=request.POST.get("name")
        getcust=bank.objects.filter(name=getname)
        bank_serializer=bankSerializer(getcust,many=True)
        return render(request,"search.html",{"data":bank_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except bank.DoesNotExist:
        return HttpResponse("Invalid title",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updatesearchapi(request):
    try:
        getname=request.POST.get("name")
        getcust=bank.objects.filter(name=getname)
        bank_serializer=bankSerializer(getcust,many=True)
        return render(request,"edit.html",{"data":bank_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except bank.DoesNotExist:
        return HttpResponse("Invalid title",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")

    getnewname=request.POST.get("newname")
    getnewaddress=request.POST.get("newaddress")
    getnewbankbalance=request.POST.get("newbankbalance")
    getnewmobile=request.POST.get("newmobile")
    getnewusername=request.POST.get("newusername")
    getnewpassword=request.POST.get("newpassword")
    mydata={'name':getnewname,'address':getnewaddress,'bankbalance':getnewbankbalance,'mobile':getnewmobile,'username':getnewusername,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    Apilink="http://127.0.0.1:8000/bank/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data has updated sucessfully")


@csrf_exempt
def deletesearchapi(request):
    try:
        getname=request.POST.get("name")
        getcust=bank.objects.filter(name=getname)
        bank_serializer=bankSerializer(getcust,many=True)
        return render(request,"delete.html",{"data":bank_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except bank.DoesNotExist:
        return HttpResponse("Invalid title",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def delete_data_read(request):
    getnewid=request.POST.get("newid")
    Apilink="http://127.0.0.1:8000/bank/view/"+getnewid
    requests.delete(Apilink)
    return HttpResponse("data has deleted sucessfully")

def adminhomepage(request):
    return render(request,'admin/adminhome.html')

def adminloginpage(request):
    return render(request,'admin/adminlogin.html')

def adminregistrationpage(request):
    return render(request,'admin/adminregistration.html')

def adminnhome(request):
    a="adminhomepage"
    if request.session.has_key('user'):
        del request.session['user']
        print("deleted")
    else:
        print("noot deleted")
    return render(request,'admin/adminhome.html',{'adminhomepage':a})

@csrf_exempt
def adminRegistration(request):
    if request.method=="POST":
        username=request.POST.get('eemail')
        data=AdminRegisterModel.objects.filter(eemail=username)
        if data:
            messages="user id exist please login"
            return redirect(adminLogin)
        else:
            print(1)
            getname=request.POST.get('ename')       
            getemail=request.POST.get('eemail')
            getpassword=request.POST.get('epassword')
            getmobile=request.POST.get('emobile')
            dict1={'ename':getname,'eemail':getemail,'epassword':getpassword,'emobile':getmobile}
            print(dict1)
            registereddata=AdminRegisterSerializer(data=dict1)
            print(registereddata)
            if registereddata.is_valid():
                registereddata.save()
                return redirect(adminLogin)
            else:
                print(registereddata.errors)
            
    return render(request,'admin/adminregistration.html')


@csrf_exempt
def adminLogin(request):
    if request.method=="POST":
        print(1)
        getusername=request.POST.get('eusername')
        getpassword=request.POST.get('epassword')
        flag=0
        data=AdminloginModel.objects.filter(eusername=getusername,epassword=getpassword)
        print(data)
        if data:
            adminserialiser=AdminloginSerializer(data,many=True)
            request.session['user']=adminserialiser.data
            print(request.session['user'])
            a="adminLogin"
            return redirect(adminheader)
    return render(request,'admin/adminlogin.html')


# def adminlogout(request):
#     if request.session.has_key('user'):
#         del request.session['user']
#     if request.session.has_key('currentplan'):
#         del request.session['currentplan']
#     return redirect(adminhomepage)