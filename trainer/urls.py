from django.urls import path
from .views import add_trainer

urlpatterns = [
    path("add/",add_trainer,name="add_trainer"),
]