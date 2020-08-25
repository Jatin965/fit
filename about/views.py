from django.shortcuts import render
from django.views.generic import TemplateView
from about import models
# Create your views here.
class HomeView(TemplateView):
    template_name = 'about/home.html'

class AboutView(TemplateView):
    template_name = 'about/about.html'

class MethodView(TemplateView):
    model = models.Job
    template_name = 'about/methods.html'
