from pages.models import Students
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from .EmailBackEnd import EmailBackEnd  #using relitive path (python 3)
from django.contrib import messages


def showTestPage(request):
    return render(request,"test.html")

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Post Method Not Allowed For Login</h2>")
    else:
        # variable to store user found. value will be None if not found
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponse("Staff Login")
            else:
                return HttpResponseRedirect('/student_home')
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")