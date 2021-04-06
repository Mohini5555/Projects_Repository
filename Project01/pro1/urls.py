<<<<<<< HEAD
"""pro1 URL Configuration
=======
"""pro2 URL Configuration
>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from pro1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('page_1/', views.page_1, name="mapping_1"),
    path('page_2/', views.page_2, name="mapping_2"),
=======
from pro2 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="mapping"),
    path('render_demo1/', views.render_demo, name="render_demo1"),
    path('render_demo2/', views.render_demo1, name="render_demo2"),

>>>>>>> 11fe4acaf6edb7e1da6191ef105be16fb11685aa
]
