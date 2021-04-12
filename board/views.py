from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from board import models
import math

LIST_COUNT = 10

def index(request):
    # 선생님 추천 page = int(request.GET.setDefault("p", 1))
    page = request.GET.get("p", 1)
    count = models.countno()
    boardlists = models.listcall(page, LIST_COUNT)
    listcount = math.ceil(count / LIST_COUNT)
    data = {
            "boardlists": boardlists,
            "count": count - (int(page) - 1) * 10,
            "listcount": listcount,
            "nextpage": int(page) + 1,
            "prvpage": int(page) - 1,
            "currpage": page,
            "next2page": int(page) + 2,
            "prv2page": int(page) - 2,
        }
    return render(request, "board/index.html", data)

def search(request):
    spage = request.GET.get("s", 1)
    try:
        kwd = request.POST["kwd"]
    except:
        kwd = request.GET.get("kwd")
    scount = models.scountno(kwd)
    sboardlists = models.searchcall(spage, LIST_COUNT, kwd)
    print(sboardlists)
    slistcount = math.ceil(scount / LIST_COUNT)
    data = {
            "sboardlists": sboardlists,
            "scount": scount - (int(spage) - 1) * 10,
            "slistcount": slistcount,
            "snextpage": int(spage) + 1,
            "sprvpage": int(spage) - 1,
            "scurrpage": spage,
            "snext2page": int(spage) + 2,
            "sprv2page": int(spage) - 2,
            "kwd": kwd
        }
    return render(request, "board/search.html", data)

def view(request):
    no = request.GET["no"]
    models.hit(no)
    results = models.contentscall(no)
    data = {
        "results" : results
    }
    return render(request, "board/view.html", data)

def updateform(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = request.GET["no"]
    results = models.contentscall(no)
    data = {
        "results": results
    }
    return render(request, "board/updateform.html", data)

def update(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = request.GET["no"]
    title = request.POST["title"]
    contents = request.POST["content"]
    models.update(title,contents,no)
    reurl = f"/board/view?no={no}"
    return HttpResponseRedirect(reurl)

def writeform(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    return render(request, "board/writeform.html")

def write(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = authuser["no"]
    title = request.POST["title"]
    contents = request.POST["content"]
    models.insert(title,contents,no)
    return HttpResponseRedirect("/board")

def delete(request):
    authuser = request.session.get("authuser")
    if authuser is None :
        return HttpResponseRedirect('/')
    no = request.GET["no"]
    models.delete(no)
    return HttpResponseRedirect("/board")

def replyform(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = request.GET["no"]
    results = models.contentscall(no)
    data = {
        "results": results
    }
    return render(request, "board/replyform.html", data)

def reply(request):
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')
    no = authuser["no"]
    title = request.POST["title"]
    contents = request.POST["content"]
    g_no = request.POST["g_no"]
    o_no = int(request.POST["o_no"]) + 1
    depth = int(request.POST["depth"]) + 1
    models.reply(title, contents, g_no, o_no, depth, no)
    return HttpResponseRedirect("/board")

