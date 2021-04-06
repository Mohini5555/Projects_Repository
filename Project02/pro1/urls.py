<<<<<<< HEAD
"""pro2 URL Configuration
=======
"""pro1 URL Configuration
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145

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
from pro2 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="mapping"),
    path('render_demo1/', views.render_demo, name="render_demo1"),
    path('render_demo2/', views.render_demo1, name="render_demo2"),

=======
from pro1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('page_1/', views.page_1, name="mapping_1"),
    path('page_2/', views.page_2, name="mapping_2"),
>>>>>>> fe32d605f5e00f7dfd3e357762f7f29eff9a6145
]
