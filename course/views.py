from django.shortcuts import render
from .forms import CourseForm

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    return render(request,"add_course.html",{"form": form})