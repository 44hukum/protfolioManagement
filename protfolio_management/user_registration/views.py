from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login 
# Create your views here.

# load another 
from django.shortcuts import redirect

def index(request):
    return render(request,'user_registration/home.html',{'signup':False})


def about(request):
     return render(request,'user_registration/AboutUs.html')

def broker(request):
    return render(request,'user_registration/broker.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('protfolio')
        
    return render(request,'user_registration/home.html',{'signup': True})

def login(request):
    if request.method=="POST": 
        u=request.POST['username']
        p=request.POST['password']
        user= authenticate(username=u,password=p)
        # user=User.objects.get(username="lp")
    
        if user is not None:
            return redirect('/protfolio')
        return render(request,'user_registration/home.html',{'signup':False,'au':True})
    return render(request,'user_registration/home.html',{'login':False})
    

def news(request):
    return render(request,'user_registration/News.html')

def applyipo(request):
    return render(request,'user_registration/ApplyIPO.html')

def ltp(request):
    return render(request,'user_registration/ltp.html')