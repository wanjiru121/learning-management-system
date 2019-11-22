from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')

def student_profile(request):
    return render(request,'profile.html')

def course_profile(request):
    return render(request,'courses.html')

