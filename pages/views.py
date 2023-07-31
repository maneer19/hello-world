from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView,name="home"):
    template_name="home.html"
class AboutPageView(TemplateView,name="about"):
    template_name = "about.html"
