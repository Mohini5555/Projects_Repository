from django.http import HttpResponse
<<<<<<< HEAD

def homepage(request):
    return HttpResponse("<h1>Hey Buddy</h1>")
    

def page_1(request):
    return HttpResponse("<marquee><h1>Welcome to Programming World</h1></marquee>")


def page_2(request):
    content = """<h1>Learn Python</h1> 
                 <h2>Learn Framework -Django</h2>"""
    return HttpResponse(content)    
       
=======
from django.shortcuts import render


def index(request):
    return HttpResponse("<marquee><h1>DJANGO - FRAMEWORK CLASS</h1></marquee>")

def render_demo(request):
    return render(request, "sample.html")  

def render_demo1(request):
    return render(request, "pro/sample.html")      
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa
