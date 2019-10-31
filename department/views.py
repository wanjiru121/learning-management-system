from django.shortcuts import render
from .forms import DepartmentForm


def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DepartmentForm()
    return render(request,"add_department.html",{"form": form})
# Create your views here.
