from django.shortcuts import render

# Create your views here.
from board import models
import math

LIST_COUNT = 10

def index(request):
    # page = request.GET["p"]
    # totalcount = models.count()
    # boardlist = models.findall(page, LIST_COUNT)
    # listcount = ceil(totalcount / LIST_COUNT)
    #
    # #paging 정보를 계산해서 제공해야함 (몇페이지가 있는지, 다음페이지는 있는지
    # data ={
    #     "boardlist" : boardlist,
    #     "listcount": listcount ,
    #     "nextpage" : 7,
    #     "prvpage" : 5,
    #     "currpage": 6,
    #
    # }
    # page = 1
    # return render(request, "board/index.html", data)
    return render(request, "board/index.html")

def view(request):
    return render(request, "board/view.html")

def updateform(request):
    return render(request, "board/updateform.html")

def writeform(request):
    return render(request, "board/writeform.html")