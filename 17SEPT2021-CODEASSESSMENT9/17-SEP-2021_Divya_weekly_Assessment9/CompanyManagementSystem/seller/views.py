from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sellerlogin(request):
    return render(request,'sellerlogin.html')

def sellerprofile(request):
    return render(request,'sellerprofile.html')