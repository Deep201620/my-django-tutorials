from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Session example
def setsession(request):
    request.session['sname'] = 'Deep Shah'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    return HttpResponse(studentname)


# Cookies example
def setcookies(request):
    response = HttpResponse("cookies is set")
    response.set_cookie("java_tutorial", 'javatpoint.com')
    return response


def getcookies(request):
    tutorial = request.COOKIES['java_tutorial']
    return HttpResponse("java tutorials @:" + tutorial);
