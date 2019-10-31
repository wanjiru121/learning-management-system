from django.db import models
from django.contrib.auth.models import User
from course.models import Course
import datetime
class Student(models.Model):
    user = models.OneToOneField(User,
        default=None,
        null=True,
        on_delete=models.CASCADE)

    gender_choices = [('M','Male'),('F','Female')]
    marital_choices = [('S','Single'),('M','Married'),('W','Widowed'),('D','Divorced'),('SE','Separated'),('P','Partnered')]
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length = 50,null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        )
    date_of_birth = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=50)
    national_id = models.SmallIntegerField()
    marital_status = models.CharField(choices=marital_choices, max_length=2,default=None)
    parent_or_guardian = models.CharField(max_length=50)
    location_of_birth = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course,blank=True)
    

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)