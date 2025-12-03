from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hwApp.urls")),
    path("lesson1/",include("hwApp.urls")),
    path("lesson2/", include("hwApp.urls")),


]
