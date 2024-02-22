from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user =auth.authenticate(username=uname , password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
           messages.info(request,"Invalid login")
           return redirect("login")
    return render(request,"login.html")
def register(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm password']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,"Email id Taken")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                 user.save();
                 return redirect('login')
                 messages.info(request, "User created")
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render (request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')