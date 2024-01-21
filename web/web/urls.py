"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('name',views.name),
    path('Button',views.Button),
    path('Pulse',views.Pulse),
    path('Heart',views.Heart),
    path('Earth',views.Earth),
    path('Bulb',views.Bulb),
    path('About',views.About),
    path('Download_resume',views.Download_resume),
    path('Web_developement',views.Web_developement),
    path('Pen_test',views.Pen_test),
    path('Flutter_tech',views.Flutter_tech),
    
]
