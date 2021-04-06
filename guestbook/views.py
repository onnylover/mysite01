from django.http import HttpResponseRedirect
from django.shortcuts import render
from guestbook import models

# Create your views here.

def index(request):
    results = models.findall()
    data = {
        "results": results
    }
    return render(request, "guestbook/index.html", data)

def add(request):
    name = request.POST["name"]
    password = request.POST["pass"]
    message = request.POST["content"]
    models.insert(name,password,message)
    return HttpResponseRedirect("/guestbook")

def deleteform(request):
    return render(request, "guestbook/deleteform.html")

def delete(request):
    no = request.POST["no"]
    password = request.POST["password"]
    models.deletebynoandpw(no, password)
    return HttpResponseRedirect("/guestbook")

