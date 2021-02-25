from django.shortcuts import render
from studapp.models import Student
from django.http import HttpResponse

# Create your views here.

def display_student_info(request):
    qs=Student.objects.all()

    #context = {'qs':qs}
    print("Inside Views Display all Method")
    #return render(request, 'studapp/studresults.html',context)
    return render(request, 'studapp/stdresultsbase.html',{'qs':qs})


def delete(request):

    sid1=int(request.GET["sid"])
    #qs=Student.objects.all().delete()[0]

    
    qs = Student.objects.filter(sid=sid1).delete()

    srec = Student.objects.get(sid=sid1)
    
    sname=request.GET["sname"]
    sm1=int(request.GET["sm1"])
    sm2=int(request.GET["sm2"])
    sm3=int(request.GET["sm3"])

    srec.sname = sname
    srec.sm1 = sm1
    srec.sm2 = sm2
    srec.sm3 = sm3
    srec.tot = sm1+sm2+sm3

    srec.save()



    html = "<html><body>Student record  is deleted </body></html>"
    return HttpResponse(html)

def create_student_info(request):
    sid=int(request.GET["sid"])
    sname=request.GET["sname"]
    sm1=int(request.GET["sm1"])
    sm2=int(request.GET["sm2"])
    sm3=int(request.GET["sm3"])
    tot=sm1+sm2+sm3
    s=Student(sid,sname,sm1,sm2,sm3,tot)
    s.save()
    print("Inside Views Create Method")
    html = "<html><body>Student record is saved </body></html>"
    return HttpResponse(html)
   
"""

def add_student_info(request):
    qs=Student.student.getorcreate()
    return render(response, "studapp/studresults.html",{"qs":qs})
"""
