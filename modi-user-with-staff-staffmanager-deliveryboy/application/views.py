from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .decorators import staff_required, staff_manager_required, delivery_boy_required


def Home(req):
    return render(req,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        flag = int(request.POST['flag'])  # Convert to integer
        
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        elif CustomUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        else:
            hashed_password = make_password(password)
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=hashed_password,
                flag=flag
            )
            user.save()
            return redirect('customer_login')  # Redirect to login page
    return render(request, 'register.html')


def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        customer = authenticate(request, username=email, password=password)  # using email as username
        
        if customer is not None:
            auth_login(request, customer)
            if customer.flag == CustomUser.STAFF:
                return redirect("staff_dashboard")
            elif customer.flag == CustomUser.STAFF_MANAGER:
                return redirect("staff_manager_dashboard")
            elif customer.flag == CustomUser.DELIVERY_BOY:
                return redirect("delivery_boy_dashboard")
            else:
                return redirect("home")  # Default redirect if no specific role found
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')



@login_required
@staff_required
def staff_dashboard(request):
    return render(request, 'dashboards/staff_dashboard.html')

@login_required
@staff_manager_required
def staff_manager_dashboard(request):
    return render(request, 'dashboards/staff_manager_dashboard.html')

@login_required
@delivery_boy_required
def delivery_boy_dashboard(request):
    return render(request, 'dashboards/delivery_boy_dashboard.html')

def logout(request):
    auth_logout(request)
    return redirect('customer_login') 