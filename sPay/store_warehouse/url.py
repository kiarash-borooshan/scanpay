from . import views
from django.urls import path

app_name = "store_warehouse"

urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("post_list/", views.post_list, name="post_list"),
    path("post_detail/<int:id_num>/", views.post_detail, name="post_detail")
]