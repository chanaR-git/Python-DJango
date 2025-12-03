from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.defaults import bad_request
from docutils.nodes import title

from hwApp.forms import AddBook
from hwApp.models import Author, Book


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
    if request.method == "POST":
        a = Author(first_name=request.POST['first_name'],last_name=request.POST['first_name'])
        a.save()
        return HttpResponse(a.__str__()+" added succesfully")
    else:
        return render(request, 'addAuthor.html')

def addbook(request):
    if request.method == "POST":
        form = AddBook(request.POST)
        if form.is_valid():
            b = Book(title=form.cleaned_data['title'],price=form.cleaned_data['price'],published=form.cleaned_data['published'],author_id=form.cleaned_data['author_id'])
            b.save()
            return HttpResponse(b.__str__()+" added succesfully")
    else:
        form = AddBook()
    return render(request,"addbook.html",{'form':form})

def navigation(request):
    data ={
        "urls":
        [
            {"title": "picture", "url": "/comp"},
            {"title": "bla bla", "url": "/html"}
        ]
    }
    return render(request,'navigation.html',data)