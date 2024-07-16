from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models  import *
from django.contrib.auth.hashers import check_password , make_password ,get_hashers
def Home(req):
    
    return render(req,'index.html')
print(make_password('1234'))
print(get_hashers_by_algorithm('1234'))

def Register(req):
    if req.method == 'POST':
        fname = req.POST.get("first_name", '')
        lname = req.POST.get("last_name", '')
        email = req.POST.get("email", '')
        username = req.POST.get("username", '')
        password = req.POST.get("password", '')
        cpassword = req.POST.get("cpassword", '')
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                print("Email already exists")
                return render(req, 'register.html', {'error': 'Email already exists'})
            elif User.objects.filter(username=username).exists():
                print("Username already exists")
                return render(req, 'register.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
                user.save()
                return redirect("Login")
        else:
            print('Password not matching')
            return render(req, 'register.html', {'error': 'Passwords do not match'})
    return render(req, 'register.html')

def login(req):
    if req.method=='POST':
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(req,user)
          print(user)
          req.session['user']=str(user)
          return redirect("home")
        else:
            print("invalid")
            return redirect('Login')
    return render(req,'login.html')

def logout(req):
    auth.logout(req)
    req.session.pop('user',None)
    return redirect('home')

def AddDetails(req,id):
    profile = User.objects.get(id=id)
    user=req.session['user']
    print(user)
    print(profile,"it is the username")
    detail = Details.objects.all()
    if req.method == 'POST':
        phonenumber = req.POST.get('phone', '')
        address = req.POST.get('address', '')
        image=req.FILES['image']
        x = Details(user=profile,phone=phonenumber,address=address,image=image)
        x.save()
        return redirect("home")
    return render(req, "userprofile.html", {"profile": profile, "detail": detail})

