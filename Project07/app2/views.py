from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to index page of app2</h2>")

def sample_view(request):
    return render(request, "sample2.html")    

def sample_app2(request):
    return render(request, "sample_app2.html")    
