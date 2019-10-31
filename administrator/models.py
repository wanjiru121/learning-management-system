from django.db import models

class Administrator(models.Model):
    gender_choices = [('M','Male'),('F','Female')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(choices=gender_choices,max_length=1,default=None)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    national_id = models.SmallIntegerField()
    user_id = models.CharField(max_length=20)



    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)
    

