from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()
router.register("v2/employees",views.EmployeeModelViewSetView,basename="memployees")
router.register("v2/tasks",views.TaskView,basename="tasks")


urlpatterns=[
    path("v2/token/",ObtainAuthToken.as_view())
    
] + router.urls