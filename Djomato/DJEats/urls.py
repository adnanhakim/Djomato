from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="djeats-home"),
    path("details/<int:restaurant_id>/", views.details, name="djeats-details-res"),
    path("details/", views.details, name="djeats-details"),
    path("search/", views.search, name="djeats-search"),
]