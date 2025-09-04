from django.urls import include, path
from rest_framework import routers
from task import views

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")

urlpatterns = [
    path("api/v1/", include(router.urls)),
   
]