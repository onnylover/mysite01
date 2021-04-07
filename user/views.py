from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from user import models


def joinform(request):
    return render(request, "user/joinform.html")

def joinsuccess(request):
    return render(request, "user/joinsuccess.html")

def join(request):
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]
    gender = request.POST["gender"]

    models.insert(name,email,password,gender)
    return HttpResponseRedirect("/user/joinsuccess")

def loginform(request):
    return render(request, "user/loginform.html")

def login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    result = models.findbyemail_and_password(email,password)

    if result is None:
        return HttpResponseRedirect("/user/loginform?result=fail")

    #로그인 처리
    request.session["authuser"] = result
    return HttpResponseRedirect("/")
    #return HttpResponse("OK")

def logout(request):
    del request.session["authuser"]
    return HttpResponseRedirect("/")

def updateform(request):
    # Access Control
    # updateform 으로 들어오는 경우 authuser 가 없으니까 에러나는데, 방어할 수 있는 소스가 있어야 함 (접근제어)
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')

    # Second way to AC
    # authuser = request.session["authuser"]
    #if "authuser" not in request.session :
    #    return HttpResponseRedirect("/")
    results = models.findbyno(authuser["no"])
    data = {"results": results}
    # result 값으로 뿌려져야 함 이름, 패스워드, 젠더, 이후에 업데이트 돌려줌
    # 있는 값은 그대로 유지, 변경된거는 업데이트 된 (기본값이 변경 안되면 그대로 감)
    return render(request, "user/updateform.html", data)

def update(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')

    no = authuser["no"]
    name = request.POST["name"]
    password = request.POST["password"]
    gender = request.POST["gender"]
    models.update(name,password,gender,no)

    return HttpResponseRedirect("/user/updatesuccess")

def updatesuccess(request):
    del request.session["authuser"]
    return render(request, "user/updatesuccess.html")
