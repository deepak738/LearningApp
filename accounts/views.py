from django.shortcuts import render , HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        if password1 == password2:
            if User.objects.filter (username= username).exists():
                messages.info(request ,'username exists')
                return redirect('register')
            elif User.objects.filter (email=email).exists():
                messages.info(request , 'email exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username , password = password1 ,email = email, first_name = first_name, last_name =last_name)
                user.save()
                messages.success(request, 'Your Details has been sent!!')
                return redirect('login')
        else:
            messages.info(request, 'password not matched!!!')
            return redirect('register')
       
    else:
        return render(request , 'register.html')
         
def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Invalid Details')
            return redirect("/")
        else:
                messages.success(request, 'Invalid Details')
                return redirect('login')
    else:

        return render(request, 'login.html' )

def logout(request):  
    auth.logout(request) 
    return redirect('/')
