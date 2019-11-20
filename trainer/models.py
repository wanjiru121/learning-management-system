from django.db import models
from django.contrib.auth.models import User

class Trainer(models.Model):
    user = models.OneToOneField(User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    gender_choices = [('M','Male'),('F','Female')]
    marital_choices = [('S','Single'),('M','Married'),('W','Widowed'),('D','Divorced'),('SE','Separated'),('P','Partnered')]
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    surname = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(choices=gender_choices,max_length=1,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    staff_number = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    department = models.ForeignKey("department.Department",null=True,on_delete=models.CASCADE,blank=True)
    national_id = models.SmallIntegerField()
    marital_status = models.CharField(choices=marital_choices,max_length=2,null=True)
    location_of_residence = models.CharField(max_length=100)


    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)



