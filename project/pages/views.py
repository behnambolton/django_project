from django.http import HttpResponse
from django.shortcuts import render

# pages/views.py
from django.views.generic import TemplateView

def showTestPage(request):
    return render(request,"test.html")

def showLoginPage(request):
    return render(request,"login_page.html")