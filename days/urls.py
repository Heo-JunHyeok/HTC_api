from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/training", views.TrainingList.as_view()),
]
