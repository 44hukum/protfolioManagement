from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'user_registration/home.html')

def help(request):
    return render(request,'user_registration/ApplyIPO.html')

def aboutus(request):
     return render(request,'user_registration/AboutUs.html')

def dmatacc(request):
    return render(request,'user_registration/Demat.html')