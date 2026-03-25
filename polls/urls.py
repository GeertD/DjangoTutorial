from django.urls import path

from . import views

urlpatterns = [
    path("goodbye", views.goodbye, name="goodbye"),
    path("", views.index, name="index")
]
