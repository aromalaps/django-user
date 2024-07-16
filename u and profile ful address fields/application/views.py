from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def Home(req):
    
    return render(req,"index.html") 
def Register(req):
    if req.method == "POST":
        name=req.POST.get('first_name','')
        lastname=req.POST.get('last_name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                print("email exist")
                return render(req,'register.html',{'error':'email exist try another email'})
            elif User.objects.filter(username=username).exists():
                print("Username exist")
                return render (req,"register.html",{'error':"Username exist"})
            else:
                user=User.objects.create_user(first_name=name,last_name=lastname,email=email,username=username,password=password)
                user.save()
                return redirect("login")
        else:
            print("password mismatch")
            return render (req,"register.html",{'error':"password missmatch"})
    return render(req,"register.html")
def Login(req):
    if req.method == "POST":
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            print(user)
            req.session['user']=str(user)
            return redirect("home")
        else:
            print("error")
            return render(req,"login.html",{"error":"invalid login"})
    return render(req,"login.html")
def Logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('home')
def UserProfiles(req,id):
        profile = User.objects.get(id=id)
        detail = UserProfile.objects.filter(username=profile)
        return render(req, "userprofile.html", {"detail":detail})

def Profiles(req, id):
    profile = User.objects.get(id=id)
    print(profile,"it is the username")
    if req.method == 'POST':
        
        phonenumber = req.POST.get('phonenumber', '')
        address = req.POST.get('address', '')
        x = UserProfile(username=profile, phonenumber=phonenumber, address=address)
        x.save()
        return redirect("profile")
    return redirect('home')






