from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.templates),
    path("firstapp/", include("firstapp.urls")),
]
