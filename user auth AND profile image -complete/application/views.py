from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib    import auth
from .models import Profile
# Create your views here.
def Home(req):
    return render(req,'index.html')
def Register(req):
    if req.method=='POST':
        name=req.POST.get('first_name','')
        lname=req.POST.get('last_name','')
        username=req.POST.get('username','')
        email=req.POST.get('email','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print("enter")
                return render(req,"register.html")
            elif User.objects.filter(email=email).exists():
                print("email")
                return render(req,"register.html")
            else:
                user=User.objects.create_user(first_name=name,last_name=lname,username=username,email=email,password=password)
                user.save()
                return redirect("home")
        else:
            print("invalid password")
            return render(req,"register.html")
    return render(req,"register.html")
def login(req):
    if req.method=="POST":
        username=req.POST.get("username",'')
        password=req.POST.get("password",'')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            req.session['user']=str(user)
            print("login success")
            return redirect("home")
        else:
            print("invlaid user")
            return render(req,"login.html")
    return render(req,"login.html")
def logout(req):
    auth.logout(req)
    req.session.pop("user",None)
    return redirect("home")
def ProfImage(req, id):
    try:
        user_obj = User.objects.get(id=id)
        profile, created = Profile.objects.get_or_create(user=req.user)
        if 'image' in req.FILES:
            profile.profilepic = req.FILES['image']  
            profile.save()
            return render(req,'userprofile.html',{"profile":profile})
    except User.DoesNotExist:
        return render(req, "userprofile.html")
    except Profile.DoesNotExist:
        return render(req, "userprofile.html")
    return render(req, "userprofile.html",{"profile":profile})