from django.shortcuts import render

from .models import Trainer
from .forms import TrainerForm

def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TrainerForm()
    return render(request,"add_trainer.html",{"form":form})
