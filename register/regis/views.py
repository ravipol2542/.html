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
            # studentinfo(request,request.user.username)
            std_info = studentinfo(request,request.user.username)
            return render(request, "regis/student.html",std_info)
            # return HttpResponseRedirect(reverse(studentinfo))
        else:
            return render(request, "regis/logintest.html",{
                "message": "Invalid credentials"
            })
    return render(request,"regis/logintest.html")

def logout_view(request):
    logout(request)
    return render(request, "regis/logintest.html",{
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
    print(sID)
    student_info = Student.objects.get(sID=sID)
    class_info  = Course.objects.filter(attendStd = student_info)
    non_classinfo = Course.objects.exclude(attendStd = student_info).all()
    logged = logout_view
    context = {'student_info':student_info,"class_info":class_info,"non_classinfo":non_classinfo,"logged1":logged,}

    return context

def enroll(request):
    if request.method == "POST":
        course = Course.objects.get(cID=request.POST["Add"])
        student = Student.objects.get(sID = request.user.username)
        course.attendStd.add(student)
        std_info = studentinfo(request,request.user.username)
        return render(request, "regis/student.html",std_info)

def withdraw(request):
    if request.method == "POST":
        course = Course.objects.get(cID=request.POST["Remove"])
        student = Student.objects.get(sID = request.user.username)
        course.attendStd.remove(student)
        std_info = studentinfo(request,request.user.username)
        return render(request, "regis/student.html",std_info)





