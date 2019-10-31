from django.urls import path
from .views import add_department

urlpatterns = [
    path("add/",add_department,name="add_department"),
]