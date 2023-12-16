from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_dept(request):
    Dno=int(input('enter deptno:'))
    Dn=input('enter dname:')
    Dl=input('enter loc:')
    DO=Dept.objects.get_or_create(Deptno=Dno,Dname=Dn,Dloc=Dl)[0]
    DO.save()
    QLTO=Dept.objects.all()
    d={'dept':QLTO}
    return render(request,'insert_dept.html',d)

def insert_Emp(request):
    Eno=int(input('enter empno:'))
    En=input('enter ename:')
    Jb=input('enter Job:')
    Hd=input('enter hiredate:')
    Sal=int(input('enter sal1:'))
    Comm=int(input('enter comm'))
    Dno=int(input('enter Deptno:'))
    DO=Dept.objects.get(Deptno=Dno)
    EO=Emp.objects.create(Empno=Eno,Ename=En,Job=Jb,Hiredate=Hd,Sal=Sal,Comm=Comm,Deptno=DO)
    EO.save()
    QLEO=Emp.objects.all()
    d={'emp':QLEO}
    return render(request,'insert_Emp.html',d)
