from django.shortcuts import render
from django.http import HttpResponse
import templates
# Create your views here.

def index(request):
    return HttpResponse("<h1>This is Index Page</h1>")

def render_demo(request):
    return render(request,"sample.html")    