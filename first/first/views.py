from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm
from services.models import Service
from django.core.paginator import Paginator

def homePage(request):
    ServicesData=Service.objects.all().order_by('-service_title')
    data={
      'SData': ServicesData 
    }
    return render(request,"index.html",data)
def Form(request):
    value=0
    fn=userForm()
    data={'Form':fn}
    try:
        if request.method == "POST":
            n1=int(request.POST.get('uname'))
            n2=int(request.POST.get('pas'))
            value=(n1+n2)
            data={
                'Form':fn,
                "value":value
            }
            return HttpResponseRedirect("/Form")

        #n1=int(request.GET['uname'])
        #n2=int(request.GET['pass'])
        #val=(n1+n2)
    except:
        pass
    return render(request,"Form.html",data)
def Cal(request):
    c=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('val1'))
            opr=request.POST.get('opr')
            n2=eval(request.POST.get('val2'))
            if opr == "+":
                c=n1+n2
            elif opr == "-":
                c=n1-n2
            elif opr == "x":
                c=n1*n2
            elif opr == "/":
                c=n1/n2
            elif opr == "%":
                c=n1%n2
    except:
        c="Invalid operator...."
    return render(request,"Cal.html",{'c':c})




def Check(request):
    fr=" "
    if request.method =="POST":
        if request.POST.get('val')=="":
            return render(request,"evenodd.html",{'res':fr})

        NUM=int(request.POST.get('val'))
        if NUM%2==0:
            fr="Even"
        else:
            fr="Odd"
    return render(request,"evenodd.html",{'res':fr})
def readmore(request):
    return render(request,"evenodd.html")