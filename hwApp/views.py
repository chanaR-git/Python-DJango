from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def text(request):
    return HttpResponse("Elul!!!!")

def html(request):

    return render(request,'index.html')

def html2(request):
    data={
        "title":"holidays ",
        "months":[("tishrei","Rosh Hashana, Yom Kipur"),
                  ("cheshvan", ""),
                  ("kislev", "chanuka")
            ]


    }
    return render(request,'les02.html',data)

def wellcome(request):
    return HttpResponse("wellcome!!!!")

def home(request):
    return HttpResponse("the url must be of the pattern: '/num of lessson/internal path'")


def layout(request):
    return render(request,'layout.html')

def comp(request):
    return render(request,'comp.html')

def addauth(request):
    return render(request,'adddAuthor.html')

def navigation(request):
    data ={
        "urls":
        [
            {"title": "picture", "url": "/comp"},
            {"title": "bla bla", "url": "/html"}
        ]
    }
    return render(request,'navigation.html',data)