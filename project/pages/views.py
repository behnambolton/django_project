from django.http import HttpResponse
from django.shortcuts import render

# pages/views.py
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = "home.html"
