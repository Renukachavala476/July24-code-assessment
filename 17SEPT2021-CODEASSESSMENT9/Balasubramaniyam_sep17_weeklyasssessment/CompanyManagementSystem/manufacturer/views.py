from django.shortcuts import redirect, render
from manufacturer.models import AdminModel,AddSellerModel
from manufacturer.serializer import AddSerializer,AdminSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def AdminRegister(request):
    if request.method=="POST":
        admindata=AdminSerializer(data=request.POST)
        if admindata.is_valid():
            admindata.save()
            print("admindatasaved")
            return render(request,'adminlogin.html')
        else:
            print(admindata.errors)
    return render(request,'adminregistration.html')
@csrf_exempt

def AdminLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        userdata=AdminModel.objects.filter(username=username,password=password)
        if userdata:
            userdetails=AdminSerializer(userdata,many=True)
            userdetails=userdetails.data
            userdetails=userdetails[0]
            print(userdetails)
            request.session['adminuser']=userdetails
            return redirect(AdminIndex)
        else:
            print("userid does not exist")
    return render(request,'adminlogin.html')
@csrf_exempt
def AdminIndex(request):
    return render(request,'adminindex.html')
@csrf_exempt
def SellerAdd(request):
    if request.method=="POST":
        sellerdata=AddSerializer(data=request.POST)
        if sellerdata.is_valid():
            sellerdata.save()
            print("Data is added")
            return redirect(viewall)
        else:
            print(sellerdata.errors)
    return render(request,'selleradd.html')
@csrf_exempt
def viewall(request):
    data=AddSellerModel.objects.all()
    return render(request,'view.html',{'data':data})

@csrf_exempt
def Sellersearch(request):
    if request.method=="POST":
        number=request.POST.get('mobile')
        data=AddSellerModel.objects.filter(mobile=number)
        print(data)
        return render(request,'adminsearch.html',{"data":data})
    return render(request,'adminsearch.html')
@csrf_exempt
def updatehtml(request):
    return render(request,'adminupdate.html')

@csrf_exempt
def Sellerupdate(request):
    if request.method=="GET":
        print(3)
        number=request.GET.get('mobile')
        print(number)
        data=AddSellerModel.objects.filter(mobile=number)
        return render(request,'adminupdate.html',{"data":data})
    if request.method=="POST":
        uid=request.POST.get('id')
        udata=AddSellerModel.objects.get(id=uid)
        print(udata)
        updatedata=AddSerializer(udata,data=request.POST)
        if updatedata.is_valid():
            updatedata.save()
            return render(request,'view.html')
        else:
            print(updatedata.errors)
    return render(request,"adminupdate.html")

@csrf_exempt
def SellerDelete(request):
    if request.method=="GET":
        number=request.GET.get('mobile')
        data=AddSellerModel.objects.filter(mobile=number)
        return render(request,'admindelete.html',{"data":data})
    if request.method=="POST":
        uid=request.POST.get('id')
        print(id)
        udata=AddSellerModel.objects.get(id=uid)
        udata.delete()
        return redirect(viewall)
    return render(request,'admindelete.html')

@csrf_exempt
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect(AdminLogin)
