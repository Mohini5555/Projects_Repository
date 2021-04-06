from django.http import HttpResponse
<<<<<<< HEAD
import os
from django.shortcuts import render

file_path = os.path.abspath(__file__)
pro_dir_path = os.path.dirname(file_path)
dir_path = os.path.dirname(pro_dir_path)


def index(request):
    return HttpResponse("<marquee direction=\"right\"><h1>Goodmorning All</h1></marquee>")


def html_respo(request):
    file_addr = os.path.join(dir_path, "sample.html")
    fp = open(file_addr, "r")
    data = fp.read()
    return HttpResponse(data)


def rend_demo(request):
    return render(request, "sample.html")


def sam_demo(request):
    return render(request, "html_demo/sample.html")
=======

def homepage(request):
    return HttpResponse("<h1>Hey Buddy</h1>")
    

def page_1(request):
    return HttpResponse("<marquee><h1>Welcome to Programming World</h1></marquee>")


def page_2(request):
    content = """<h1>Learn Python</h1> 
                 <h2>Learn Framework -Django</h2>"""
    return HttpResponse(content)    
       
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145
