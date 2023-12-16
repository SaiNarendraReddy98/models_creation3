from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Dloc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.Deptno)

class Emp(models.Model):
    Empno=models.IntegerField(unique=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField(null=True,blank=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ename


    