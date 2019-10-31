from rest_framework import routers
from .views import StudentViewSet,TrainerViewSet,CourseViewSet,DepartmentViewSet,LessonPlanViewSet,AssignmentViewSet
from django.urls import path,include


router = routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("trainers",TrainerViewSet)
router.register("courses",CourseViewSet)
router.register("departments",DepartmentViewSet)
router.register("lessons", LessonPlanViewSet)
router.register("assignments",AssignmentViewSet)
urlpatterns = [
    path("",include(router.urls)),
]



