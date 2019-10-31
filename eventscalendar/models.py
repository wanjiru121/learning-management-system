from django.db import models


class Event(models.Model):
    status_choices = [('CO','Confirmed'),('PE','Pending'),('CA','Cancelled')]
    name = models.CharField(max_length=50)
    description = models.TextField()
    confirmation_status = models.CharField(choices=status_choices,max_length=2,default=None)
    date = models.DateField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    contact = models.EmailField()



    def __str__(self):
        return '{}'.format(self.name)

# Create your models here.
