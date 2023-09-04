from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is Home Page")


def templates(request):
    return render(request, "index.html", {"author": "Glen Maxwell"})


def templatesabout(request):
    return render(request, "about.html", {"author": "Glen Maxwell"})
