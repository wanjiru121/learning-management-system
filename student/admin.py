from django.contrib import admin
from .models import Student
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Student)

admin.site.unregister(Group)
