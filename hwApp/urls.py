
from django.urls import path

from hwApp import views

urlpatterns = [
    path("text/", views.text),
    path("html/", views.html),
    path("html2",views.html2),
    path("", views.home),
    path("layout", views.layout),
    path("comp", views.comp),
    path("bootstrap", views.navigation),
    path("addauthor", views.addauth),
]
