from django.shortcuts import render,redirect
from manufacturer.models import AddSellerModel
from manufacturer.serializer import AddSerializer,AdminSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        userdata=AddSellerModel.objects.filter(username=username,password=password)
        if userdata:
            userdetails=AddSerializer(userdata,many=True)
            userdetails=userdetails.data
            userdetails=userdetails[0]
            print(userdetails)
            request.session['user']=userdetails
            return redirect(Index)
    return render(request,'login.html')
@csrf_exempt
def Index(request):
    userdata=request.session['user']
    data=AddSellerModel.objects.filter(id=userdata['id'])
    return render(request,'index.html',{'data':data})

@csrf_exempt
def changepassword(request):
    passwordtag="a"
    userdata=request.session['user']
    data=AddSellerModel.objects.filter(id=userdata['id'])
    if request.method=="POST":
        id=request.POST.get('id')
        password=request.POST.get('password')
        print(id,password)
        data=AddSellerModel.objects.filter(id=id).update(password=password)
        print(data)
        return redirect(Index)
    return render(request,'index.html',{"password":passwordtag,'data':data})

@csrf_exempt
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return redirect(login)