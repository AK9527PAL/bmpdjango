from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import Admission_Form

# Create your views here.

def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def gallery(request):
    return render(request,"gallery.html")


def Contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        new_contact=Contact(name=name,email=email,phone=phone,desc=desc)
        new_contact.save()
    return render(request,"contact.html")


def timetable1(request):
    return render(request,"timetable1.html")


def timetable2(request):
    return render(request,"timetable2.html")


def timetable3(request):
    return render(request,"timetable3.html")


def timetable4(request):
    return render(request,"timetable4.html")


def preprimary(request):
    return render(request,"preprimary.html")

def Middle(request):
    return render(request,"Middle.html")

def Secondary(request):
    return render(request,"Secondary.html")

def Srsecondary(request):
    return render(request,"Srsecondary.html")

def Rules(request):
    return render(request,"Rules.html")

def Tc(request):
    return render(request,"Tc.html")

def Admission_Procedure(request):
    return render(request,"Admission-Procedure.html")

def Fee_Structure(request):
    return render(request,"Fee-Structure.html")

def Admission_Form(request):
    if request.method=="POST":
        print(request.POST)

        myname=request.POST.get('name')
        dob=request.POST.get('dob')
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        gender=request.POST.get('gender')
        branch=request.POST.get('branch')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        add=request.POST.get('add')
        form=Admission_Form(name=myname,dob=dob,fame=fname,mname=mname,gender=gender,branch=branch,email=email,phone=phone,add=add)
        form.save()


    return render(request,"Admission-Form.html")


def developer(request):
    return render(request,"developer.html")

