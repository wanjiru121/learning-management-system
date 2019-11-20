from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField(max_length=10,help_text="format: YYYY-MM-DD",null=True)
    end_date = models.DateField(max_length=10,help_text="format: YYYY-MM-DD",null=True)
    course_email = models.EmailField()
    trainer = models.ForeignKey("trainer.Trainer",null=True,on_delete=models.CASCADE)
    department = models.ForeignKey("department.Department",null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.course_title)


class LessonPlan(models.Model):
    course = models.ForeignKey("course.Course",null=True,on_delete=models.SET_NULL,blank=True)
    lesson_title = models.CharField(max_length=50)
    lesson_sub_title = models.CharField(max_length=50)
    objectives = models.TextField()
    materials_needed = models.TextField()
    lesson_content = models.FileField(upload_to='documents/',null=True)
    def __str__(self):
        return '{}'.format(self.lesson_title)




class Assignment(models.Model):
    lesson = models.ForeignKey("course.LessonPlan",null=True,on_delete=models.SET_NULL,blank=True)
    type_choices = [('I','Individual'),('G','Group')]
    name = models.CharField(max_length=50)
    instructions = models.TextField()
    assignment_document = models.FileField(upload_to='documents/')
    assignment_type = models.CharField(choices=type_choices,max_length=1,default=None)
    possible_points = models.SmallIntegerField()
    start_date = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Attendace(models.Model):
    attendance_choices = [('P','Present'),('A','Absent'),('L','Late'),('E','Excused')]
    name_of_the_course = models.CharField(max_length=50)
    name_of_the_student = models.CharField(max_length=50)
    attendace_status = models.CharField(choices=attendance_choices,max_length=1,default=None)

class CourseCalendar(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    contact = models.EmailField()