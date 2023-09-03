from django.http import HttpResponse

from django.shortcuts import render


def homepage(request):
    return HttpResponse("This is Main Home Paged")


def templates(request):
    return render(request, "base.html")
