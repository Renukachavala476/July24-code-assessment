from django.shortcuts import render
def myHome(request):
    return render(request,'home.html')