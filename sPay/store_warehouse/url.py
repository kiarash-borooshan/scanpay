from . import views
from django.urls import path

app_name = "store_warehouse"

urlpatterns = [
    path("post_list/", views.post_list, name="post_list")
]