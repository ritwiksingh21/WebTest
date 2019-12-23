from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.simple_upload, name="upload")
]
