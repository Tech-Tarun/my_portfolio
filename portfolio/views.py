from django.http import HttpResponse
from django.shortcuts import render
from .models import Details
import string


def index(request):
    return render(request, "portfolio/index.html")

def Analyse(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,subject,message)
        obj=Details()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
    return render(request,"portfolio/index1.html")