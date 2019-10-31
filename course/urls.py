from django.urls import path
from .views import add_course

urlpatterns = [
    path("add/",add_course,name="add_course"),
]