from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages,auth
from .models import User

def Home(req):
    return render(req, 'index.html')

def register(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        phone=req.POST.get("phone","")
        email=req.POST.get("email","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        p_image=req.FILES['image'] 

        if password==cpassword:
            print("password verified")
            if User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fname,phone=phone,email=email,prof_image=p_image,password=password)
                user.save()
                return redirect("login")
        else:
            messages.error(req, "Passwords do not match")
            return render(req, 'registration.html')
    
    return render(req, "registration.html")

def login(req):
    if req.method=='POST':
        email=req.POST.get("email","")
        password=req.POST.get("password","")
        user=auth.authenticate(email=email,password=password)
        print(user.first_name)
        if user is not None:
          auth.login(req,user)
          req.session['user']=str(user)
          return redirect("home")
        else:
            messages.info(req, "invalidcredentials")
          
            return redirect('login')
    return render(req,'login.html')
def logout(req):
    
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('home')
def UserProfile(req,id):
    user=req.session['user']
    profile=User.objects.get(id=id)
    print(profile.first_name)
    return render(req,'profile.html',{'profile':profile})