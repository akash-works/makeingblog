from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        email=request.post.get("email")
        email.save()

    return render(request,"index.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("text")
        a = User(name=name,email=email,phone=phone,message=message)
        a.save()

    return render (request,"contact.html")