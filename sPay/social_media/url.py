from django.urls import path

from . import views


app_name = "social_media"

urlpatterns = [
    path("", views.video_call, name="video_call"),
]