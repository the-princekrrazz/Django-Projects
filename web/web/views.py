from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def name(request):
    return render(request,"name.html")
def Button(request):
    return render(request,"Button.html")
def Pulse(request):
    return render(request,"Pulse.html")
def Heart(request):
    return render(request,"Herat.html")
def Earth(request):
    return render(request,"Earth.html")
def Bulb(request):
    return render(request,"Bulb.html")
def About(request):
    return render(request,"readmore.html")
def Download_resume(request):
    return render(request,"resume.html")
def Web_developement(request):
    return render(request,"Webdev.html")
def Pen_test(request):
    return render(request,"Pentesting.html")
def Flutter_tech(request):
    return render(request,"FlutterTech.html")