from django.db import models

# Create your models here.
class Student(models.Model):
    sName = models.CharField(max_length = 64)
    sID = models.CharField(max_length = 10 )
    def __str__(self):
        return f"{self.sID}"
class Course(models.Model):
    cID = models.CharField(max_length = 5)
    cName = models.CharField(max_length = 64)
    cTerm = models.PositiveIntegerField()
    cYear = models.CharField(max_length = 4)
    avaiable_seat = models.PositiveIntegerField(default = 3)
    status = models.BooleanField(default=True)
    attendStd = models.ManyToManyField(Student,blank=True)
    
    def seatCheck(self):
        if self.avaiable_seat > len(self.attendStd):
            return self.status == True
        else:
            return self.status == False
    
    
    def statusCheck(self):
        if self.status == True:
            return "Available"
        else:
            return "Closed"
            
   
    def __str__(self):
        return f"{self.cID}:{self.cName} Semester {self.cTerm} Academic year:{self.cYear}"




