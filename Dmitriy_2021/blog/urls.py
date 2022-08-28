from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("blog/",views.blog_index, name="blog_index"),
    path("blog/<int:pk>/",views.blog_detail, name="blog_detail"),
]