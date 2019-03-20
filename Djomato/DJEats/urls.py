from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="djeats-home"),
    path("", views.details, name="djeats-details"),
]