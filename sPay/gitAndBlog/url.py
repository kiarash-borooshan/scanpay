from django.urls import path

from . import views


app_name = "gitAndBlog"

urlpatterns = [
    path("", views.git_blog, name="git_blog")
]