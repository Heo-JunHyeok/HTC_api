from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/healthlist", views.HealthList.as_view()),
    path("api/v1/healthlist/<int:pk>", views.HealthDetail.as_view()),
    path("api/v1/daily", views.DailyHealth.as_view()),
]
