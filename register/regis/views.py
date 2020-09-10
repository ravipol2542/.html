from django.shortcuts import render
from django.http import HttpResponse
from .models import Course,Student
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "regis/login.html",{
                "message": "Invalid credentials"
            })
    return studentinfo(request,request.user.username)

def logout_view(request):
    logout(request)
    return render(request, "regis/login.html",{
        "message": "Logged out"
    })


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse(login))
    return render(request , "regis/student.html")

def classcourse(request):
    classinfo = Course.objects.all() #ดึงค่าจากdatabaseมาทั้งหมด

    context = {'classinfo':classinfo}
    return render(request,'regis/classcourse.html',context)

def studentinfo(request,sID):
    student_info = Student.objects.get(sID=sID)
    class_info  = Course.objects.filter(attendStd = student_info)
    non_classinfo = Course.objects.exclude(attendStd = student_info).all()
    logged = logout_view
    context = {'student_info':student_info,"class_info":class_info,"non_classinfo":non_classinfo,"logged1":logged,}

    return render(request,'regis/student.html',context)

def enroll(request, sID):
    pass



