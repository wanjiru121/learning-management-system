from django.urls import path
from .views import home_view
from .views import student_profile,course_profile,dashboard_profile



urlpatterns = [
    path('',home_view,name="home_view"),
    path('profile/',student_profile,name="student_profile"),
    path('course/',course_profile,name="course_profile"),
    path('dashboard/',dashboard_profile,name="dashboard_profile"),
]