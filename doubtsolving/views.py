from django.shortcuts import render , HttpResponse,redirect
from datetime import datetime
from doubtsolving.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    
    return render(request, 'index.html', )
   

def about(request):
    
    return render(request, 'about.html' )

def services(request):

    return render(request, 'services.html' )


def bookfreedemo(request):
    
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        bookfreedemo = Contact(name= name ,email=email , phone= phone, desc=desc, date= datetime.today())
        bookfreedemo.save()
        messages.success(request, 'Your Details has been sent!!')
    return render(request, 'bookfreedemo.html' )