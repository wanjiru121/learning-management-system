from django.urls import path
from .views import add_event

urlpatterns = [
    path("add/",add_event,name="add_event"),
]