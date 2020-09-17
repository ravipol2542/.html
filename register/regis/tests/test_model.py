from django.test import TestCase
from ..models import  Student,Course
# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        #createStudent
        s1 = Student.objects.create(sName="Jamie Vardy", sID="6110612998")
        s2 = Student.objects.create(sName="Michael Owen",sID="6110613004")
        s3 = Student.objects.create(sName="Oliver Kahn",sID="6110613104")
        #createCourse
        a1=Course.objects.create(cID="CN201",cName="DATA I",cYear="2020",cTerm=2,avaiable_seat=1, )
        a2=Course.objects.create(cID="CN202",cName="DATA II",cYear="2020",cTerm=2,avaiable_seat=2,)
        


    def test_enroll_Total(self):
        a = Course.objects.get(cID="CN201")
        s = Student.objects.get(sName="Jamie Vardy")
        a.attendStd.add(s)
        self.assertEqual(a.attendStd.count(),1)
    
    def test_enroll_status(self):
        a = Course.objects.get(cID="CN202")
        s1 = Student.objects.get(sName="Jamie Vardy")
        s2 = Student.objects.get(sName="Michael Owen")
        a.attendStd.add(s1)
        a.attendStd.add(s2)
        a.status = a.seatCheck()
        self.assertFalse(a.status)

    def test_seat_left(self):
        a = Course.objects.get(cID="CN201")
        s1 = Student.objects.get(sName="Jamie Vardy")
        a.attendStd.add(s1)
        self.assertEqual(int(a.seatLeft()),0)
